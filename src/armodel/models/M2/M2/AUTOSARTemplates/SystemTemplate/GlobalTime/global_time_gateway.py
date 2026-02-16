"""GlobalTimeGateway AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import (
    GlobalTimeMaster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_slave import (
    GlobalTimeSlave,
)


class GlobalTimeGateway(Identifiable):
    """AUTOSAR GlobalTimeGateway."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "host": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EcuInstance,
        ),  # host
        "master": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=GlobalTimeMaster,
        ),  # master
        "slave": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=GlobalTimeSlave,
        ),  # slave
    }

    def __init__(self) -> None:
        """Initialize GlobalTimeGateway."""
        super().__init__()
        self.host: Optional[EcuInstance] = None
        self.master: Optional[GlobalTimeMaster] = None
        self.slave: Optional[GlobalTimeSlave] = None


class GlobalTimeGatewayBuilder:
    """Builder for GlobalTimeGateway."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeGateway = GlobalTimeGateway()

    def build(self) -> GlobalTimeGateway:
        """Build and return GlobalTimeGateway object.

        Returns:
            GlobalTimeGateway instance
        """
        # TODO: Add validation
        return self._obj
