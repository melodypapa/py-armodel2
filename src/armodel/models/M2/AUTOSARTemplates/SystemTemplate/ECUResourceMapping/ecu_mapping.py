"""ECUMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 182)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_ECUResourceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping.hw_port_mapping import (
    HwPortMapping,
)


class ECUMapping(Identifiable):
    """AUTOSAR ECUMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    comm_controllers: list[Any]
    ecu: Optional[HwElement]
    ecu_instance: Optional[EcuInstance]
    hw_port_mapping_ref: ARRef
    def __init__(self) -> None:
        """Initialize ECUMapping."""
        super().__init__()
        self.comm_controllers: list[Any] = []
        self.ecu: Optional[HwElement] = None
        self.ecu_instance: Optional[EcuInstance] = None
        self.hw_port_mapping_ref: ARRef = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ECUMapping":
        """Deserialize XML element to ECUMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ECUMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse comm_controllers (list)
        obj.comm_controllers = []
        for child in ARObject._find_all_child_elements(element, "COMM-CONTROLLERS"):
            comm_controllers_value = child.text
            obj.comm_controllers.append(comm_controllers_value)

        # Parse ecu
        child = ARObject._find_child_element(element, "ECU")
        if child is not None:
            ecu_value = ARObject._deserialize_by_tag(child, "HwElement")
            obj.ecu = ecu_value

        # Parse ecu_instance
        child = ARObject._find_child_element(element, "ECU-INSTANCE")
        if child is not None:
            ecu_instance_value = ARObject._deserialize_by_tag(child, "EcuInstance")
            obj.ecu_instance = ecu_instance_value

        # Parse hw_port_mapping_ref
        child = ARObject._find_child_element(element, "HW-PORT-MAPPING")
        if child is not None:
            hw_port_mapping_ref_value = ARObject._deserialize_by_tag(child, "HwPortMapping")
            obj.hw_port_mapping_ref = hw_port_mapping_ref_value

        return obj



class ECUMappingBuilder:
    """Builder for ECUMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ECUMapping = ECUMapping()

    def build(self) -> ECUMapping:
        """Build and return ECUMapping object.

        Returns:
            ECUMapping instance
        """
        # TODO: Add validation
        return self._obj
