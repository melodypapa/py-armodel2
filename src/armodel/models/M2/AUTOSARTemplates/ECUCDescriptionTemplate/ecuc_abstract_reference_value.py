"""EcucAbstractReferenceValue AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_indexable_value import (
    EcucIndexableValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.MSR.Documentation.Annotation.annotation import (
    Annotation,
)


class EcucAbstractReferenceValue(EcucIndexableValue):
    """AUTOSAR EcucAbstractReferenceValue."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("annotations", None, False, True, Annotation),  # annotations
        ("definition", None, False, False, any (EcucAbstractReference)),  # definition
        ("is_auto_value", None, True, False, None),  # isAutoValue
    ]

    def __init__(self) -> None:
        """Initialize EcucAbstractReferenceValue."""
        super().__init__()
        self.annotations: list[Annotation] = []
        self.definition: Optional[Any] = None
        self.is_auto_value: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucAbstractReferenceValue to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucAbstractReferenceValue":
        """Create EcucAbstractReferenceValue from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucAbstractReferenceValue instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucAbstractReferenceValue since parent returns ARObject
        return cast("EcucAbstractReferenceValue", obj)


class EcucAbstractReferenceValueBuilder:
    """Builder for EcucAbstractReferenceValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucAbstractReferenceValue = EcucAbstractReferenceValue()

    def build(self) -> EcucAbstractReferenceValue:
        """Build and return EcucAbstractReferenceValue object.

        Returns:
            EcucAbstractReferenceValue instance
        """
        # TODO: Add validation
        return self._obj
