"""CanTpEcu AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)


class CanTpEcu(ARObject):
    """AUTOSAR CanTpEcu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("cycle_time_main", None, True, False, None),  # cycleTimeMain
        ("ecu_instance", None, False, False, EcuInstance),  # ecuInstance
    ]

    def __init__(self) -> None:
        """Initialize CanTpEcu."""
        super().__init__()
        self.cycle_time_main: Optional[TimeValue] = None
        self.ecu_instance: Optional[EcuInstance] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CanTpEcu to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanTpEcu":
        """Create CanTpEcu from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CanTpEcu instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CanTpEcu since parent returns ARObject
        return cast("CanTpEcu", obj)


class CanTpEcuBuilder:
    """Builder for CanTpEcu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanTpEcu = CanTpEcu()

    def build(self) -> CanTpEcu:
        """Build and return CanTpEcu object.

        Returns:
            CanTpEcu instance
        """
        # TODO: Add validation
        return self._obj
