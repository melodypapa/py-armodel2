"""DynamicPartAlternative AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu import (
    ISignalIPdu,
)


class DynamicPartAlternative(ARObject):
    """AUTOSAR DynamicPartAlternative."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("initial_dynamic", None, True, False, None),  # initialDynamic
        ("i_pdu", None, False, False, ISignalIPdu),  # iPdu
        ("selector_field", None, True, False, None),  # selectorField
    ]

    def __init__(self) -> None:
        """Initialize DynamicPartAlternative."""
        super().__init__()
        self.initial_dynamic: Optional[Boolean] = None
        self.i_pdu: Optional[ISignalIPdu] = None
        self.selector_field: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DynamicPartAlternative to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DynamicPartAlternative":
        """Create DynamicPartAlternative from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DynamicPartAlternative instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DynamicPartAlternative since parent returns ARObject
        return cast("DynamicPartAlternative", obj)


class DynamicPartAlternativeBuilder:
    """Builder for DynamicPartAlternative."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DynamicPartAlternative = DynamicPartAlternative()

    def build(self) -> DynamicPartAlternative:
        """Build and return DynamicPartAlternative object.

        Returns:
            DynamicPartAlternative instance
        """
        # TODO: Add validation
        return self._obj
