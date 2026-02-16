"""LinMaster AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_slave_config import (
    LinSlaveConfig,
)


class LinMaster(ARObject):
    """AUTOSAR LinMaster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "lin_slaves": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=LinSlaveConfig,
        ),  # linSlaves
        "time_base": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeBase
        "time_base_jitter": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeBaseJitter
    }

    def __init__(self) -> None:
        """Initialize LinMaster."""
        super().__init__()
        self.lin_slaves: list[LinSlaveConfig] = []
        self.time_base: Optional[TimeValue] = None
        self.time_base_jitter: Optional[TimeValue] = None


class LinMasterBuilder:
    """Builder for LinMaster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinMaster = LinMaster()

    def build(self) -> LinMaster:
        """Build and return LinMaster object.

        Returns:
            LinMaster instance
        """
        # TODO: Add validation
        return self._obj
