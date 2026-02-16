"""TtcanCluster AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    TimeValue,
)


class TtcanCluster(ARObject):
    """AUTOSAR TtcanCluster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("basic_cycle_length", None, True, False, None),  # basicCycleLength
        ("ntu", None, True, False, None),  # ntu
        ("operation_mode", None, True, False, None),  # operationMode
    ]

    def __init__(self) -> None:
        """Initialize TtcanCluster."""
        super().__init__()
        self.basic_cycle_length: Optional[Integer] = None
        self.ntu: Optional[TimeValue] = None
        self.operation_mode: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TtcanCluster to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TtcanCluster":
        """Create TtcanCluster from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TtcanCluster instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TtcanCluster since parent returns ARObject
        return cast("TtcanCluster", obj)


class TtcanClusterBuilder:
    """Builder for TtcanCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TtcanCluster = TtcanCluster()

    def build(self) -> TtcanCluster:
        """Build and return TtcanCluster object.

        Returns:
            TtcanCluster instance
        """
        # TODO: Add validation
        return self._obj
