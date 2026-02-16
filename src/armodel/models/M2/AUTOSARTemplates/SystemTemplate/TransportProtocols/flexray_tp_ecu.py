"""FlexrayTpEcu AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)


class FlexrayTpEcu(ARObject):
    """AUTOSAR FlexrayTpEcu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("cancellation", None, True, False, None),  # cancellation
        ("cycle_time_main", None, True, False, None),  # cycleTimeMain
        ("ecu_instance", None, False, False, EcuInstance),  # ecuInstance
        ("full_duplex", None, True, False, None),  # fullDuplex
    ]

    def __init__(self) -> None:
        """Initialize FlexrayTpEcu."""
        super().__init__()
        self.cancellation: Optional[Boolean] = None
        self.cycle_time_main: Optional[TimeValue] = None
        self.ecu_instance: Optional[EcuInstance] = None
        self.full_duplex: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FlexrayTpEcu to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayTpEcu":
        """Create FlexrayTpEcu from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FlexrayTpEcu instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FlexrayTpEcu since parent returns ARObject
        return cast("FlexrayTpEcu", obj)


class FlexrayTpEcuBuilder:
    """Builder for FlexrayTpEcu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayTpEcu = FlexrayTpEcu()

    def build(self) -> FlexrayTpEcu:
        """Build and return FlexrayTpEcu object.

        Returns:
            FlexrayTpEcu instance
        """
        # TODO: Add validation
        return self._obj
