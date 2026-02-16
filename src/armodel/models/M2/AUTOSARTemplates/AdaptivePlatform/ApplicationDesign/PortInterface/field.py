"""Field AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class Field(AutosarDataPrototype):
    """AUTOSAR Field."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("has_getter", None, True, False, None),  # hasGetter
        ("has_notifier", None, True, False, None),  # hasNotifier
        ("has_setter", None, True, False, None),  # hasSetter
    ]

    def __init__(self) -> None:
        """Initialize Field."""
        super().__init__()
        self.has_getter: Optional[Boolean] = None
        self.has_notifier: Optional[Boolean] = None
        self.has_setter: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Field to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Field":
        """Create Field from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Field instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Field since parent returns ARObject
        return cast("Field", obj)


class FieldBuilder:
    """Builder for Field."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Field = Field()

    def build(self) -> Field:
        """Build and return Field object.

        Returns:
            Field instance
        """
        # TODO: Add validation
        return self._obj
