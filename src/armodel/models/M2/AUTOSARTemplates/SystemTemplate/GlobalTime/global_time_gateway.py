"""GlobalTimeGateway AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 861)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    host: Optional[EcuInstance]
    master: Optional[GlobalTimeMaster]
    slave: Optional[GlobalTimeSlave]
    def __init__(self) -> None:
        """Initialize GlobalTimeGateway."""
        super().__init__()
        self.host: Optional[EcuInstance] = None
        self.master: Optional[GlobalTimeMaster] = None
        self.slave: Optional[GlobalTimeSlave] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeGateway":
        """Deserialize XML element to GlobalTimeGateway object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeGateway object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse host
        child = ARObject._find_child_element(element, "HOST")
        if child is not None:
            host_value = ARObject._deserialize_by_tag(child, "EcuInstance")
            obj.host = host_value

        # Parse master
        child = ARObject._find_child_element(element, "MASTER")
        if child is not None:
            master_value = ARObject._deserialize_by_tag(child, "GlobalTimeMaster")
            obj.master = master_value

        # Parse slave
        child = ARObject._find_child_element(element, "SLAVE")
        if child is not None:
            slave_value = ARObject._deserialize_by_tag(child, "GlobalTimeSlave")
            obj.slave = slave_value

        return obj



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
