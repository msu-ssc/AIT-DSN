import dataclasses
import os
import shutil
import sys
from pathlib import Path
import threading
from typing import TYPE_CHECKING, Generator

import pytest

if TYPE_CHECKING:
    from ait.core.cfg import AitConfig


@pytest.fixture(scope="package")
def cfdp_environment():
    """Fixture that sets environment variables for AIT_ROOT and AIT_CONFIG and monkeys around with the path to allow importing the AIT package."""
    os.environ["AIT_TEST"] = "1"

    ait_root_path = Path(__file__).parent
    ait_config_path = Path(__file__).parent / "config.yaml"
    os.environ["AIT_ROOT"] = str(ait_root_path)
    os.environ["AIT_CONFIG"] = str(ait_config_path)

    # Add the AIT package to the path
    workspace_path = Path(os.getcwd()).parent
    sys.path.insert(0, str(workspace_path))
    yield


# def test_stuff(cfdp_environment):
    # assert True


def test_environment(cfdp_environment: None):
    from ait.dsn.cfdp.cfdp import CFDP

    assert CFDP is not None

@dataclasses.dataclass
class DatasinkPathInfo:
    outgoing_path: Path
    incoming_path: Path
    tempfiles_path: Path
    pdusink_path: Path
    mib_path: Path

    def all_paths(self) -> list[Path]:
        """Return all paths in the datasink, including the MIB."""
        return [
            self.outgoing_path,
            self.incoming_path,
            self.tempfiles_path,
            self.pdusink_path,
            self.mib_path,
        ]

    def delete_all_folders(self):
        """Completely delete all paths in the datasink, recursively."""
        for path in self.all_paths():
            assert path is not None, f"Path {path} is None"

            if path.exists() and path.is_dir():
                shutil.rmtree(path)
            elif path.exists() and path.is_file():
                path.unlink()
            assert not path.exists(), f"Failed to delete {path}"

    def create_all_folders(self, pave: bool = True):
        """Create all paths in the datasink, recursively. Optionally delete existing paths first."""
        if pave:
            self.delete_all_folders()
        

        for path in self.all_paths():
            assert path is not None, f"Path {path} is None"

            path.mkdir(parents=True, exist_ok=True)
            assert path.exists(), f"Failed to create {path}"
        

@pytest.fixture(scope="package")
def datasink(cfdp_environment: None) -> Generator[DatasinkPathInfo, None, None]:
    import ait.core # Have to import this because it creates ait.config as a side-effect,
                    # even though the linter doesn't understand that.
    
    ait_config: AitConfig = ait.config
    ait_config.get("dsn.cfdp.datasink.outgoing.path")
    assert ait_config is not None

    outgoing_path = ait_config.get("dsn.cfdp.datasink.outgoing.path")
    incoming_path = ait_config.get("dsn.cfdp.datasink.incoming.path")
    tempfiles_path = ait_config.get("dsn.cfdp.datasink.tempfiles.path")
    pdusink_path = ait_config.get("dsn.cfdp.datasink.pdusink.path")
    mib_path = ait_config.get("dsn.cfdp.mib.path")

    assert outgoing_path is not None, f"Failed to get outgoing path from {ait_config=}"
    assert incoming_path is not None, f"Failed to get incoming path from {ait_config=}"
    assert tempfiles_path is not None, f"Failed to get tempfiles path from {ait_config=}"
    assert pdusink_path is not None, f"Failed to get pdusink path from {ait_config=}"
    assert mib_path is not None, f"Failed to get mib path from {ait_config=}"
    
    info = DatasinkPathInfo(
        outgoing_path=Path(outgoing_path),
        incoming_path=Path(incoming_path),
        tempfiles_path=Path(tempfiles_path),
        pdusink_path=Path(pdusink_path),
        mib_path=Path(mib_path),
    )

    yield info

    # Cleanup after the test
    info.delete_all_folders()


def test_create_datasink(datasink: DatasinkPathInfo):
    """Test the creation of the datasink."""
    assert datasink is not None
    assert datasink.outgoing_path is not None
    assert datasink.incoming_path is not None
    assert datasink.tempfiles_path is not None
    assert datasink.pdusink_path is not None
    assert datasink.mib_path is not None

    datasink.delete_all_folders()
    datasink.create_all_folders()

    # Check that all paths exist and are directories
    for path in [datasink.outgoing_path, datasink.incoming_path, datasink.tempfiles_path, datasink.pdusink_path, datasink.mib_path]:
        assert path.exists(), f"Path {path} does not exist"
        assert path.is_dir(), f"Path {path} is not a directory"
    

def test_cfdp_send(datasink: DatasinkPathInfo):
    """Test the CFDP send functionality."""
    import gevent
    from ait.dsn.cfdp.cfdp import CFDP, TransmissionMode

    # Create the datasink folders
    datasink.create_all_folders(pave=True)

    outgoing_relative_path = "cfdp_class_1_out.txt"
    outgoing_path = datasink.outgoing_path / outgoing_relative_path
    incoming_relative_path = "cfdp_class_1_in.txt"

    sender_id = 1
    receiver_id = 2

    # Create the outgoing file
    assert not outgoing_path.exists(), f"Outgoing path {outgoing_path} already exists"
    outgoing_path.parent.mkdir(parents=True, exist_ok=True)
    if outgoing_path.exists():
        outgoing_path.unlink()
    text = "DavidClarkeMayo!"
    outgoing_path.write_text(text, encoding="ascii")
    assert outgoing_path.exists(), f"Outgoing path {outgoing_path} does not exist"
    assert outgoing_path.is_file(), f"Outgoing path {outgoing_path} is not a file"
    assert outgoing_path.read_text(encoding="ascii") == text, f"Outgoing path {outgoing_path} does not contain expected text {text!r}"

    # # Start the receiver first
    # class ReceiverThread(threading.Thread):
    #     def __init__(self, receiver_id: int):
    #         super().__init__(daemon=True)
    #         self.receiver_id = receiver_id

    #     def run(self):
    #         cfdp_receiver = CFDP(self.receiver_id)
    #         cfdp_receiver.connect(('localhost', 8002), send_host=('localhost', 8003))

    # # cfdp_receiver = CFDP(receiver_id)
    # # cfdp_receiver.connect(('localhost', 9002), send_host=('localhost', 9003))
    # receiver_thread = ReceiverThread(receiver_id)
    # receiver_thread.start()

    # Start the sender
    cfdp_sender = CFDP(sender_id)
    cfdp_sender.connect(('localhost', 8003), send_host=('localhost', 8002))

    destination_id = receiver_id
    source_file = outgoing_relative_path
    destination_file = incoming_relative_path
    
    # Sleep a few seconds to allow the receiver to start
    # Maybe not necessary?
    gevent.sleep(1)
    cfdp_sender.put(destination_id, source_file, destination_file, transmission_mode=TransmissionMode.NO_ACK)
    
    # Sleep a few seconds to allow the receiver to start
    # Maybe not necessary?
    gevent.sleep(10)

    pass