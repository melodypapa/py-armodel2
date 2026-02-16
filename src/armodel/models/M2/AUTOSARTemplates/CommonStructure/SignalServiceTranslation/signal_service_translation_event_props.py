"""SignalServiceTranslationEventProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class SignalServiceTranslationEventProps(Identifiable):
    """AUTOSAR SignalServiceTranslationEventProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("element_propses", None, False, True, any (SignalService)),  # elementPropses
        ("safe_translation", None, True, False, None),  # safeTranslation
        ("secure", None, True, False, None),  # secure
        ("translation", None, False, False, VariableDataPrototype),  # translation
    ]

    def __init__(self) -> None:
        """Initialize SignalServiceTranslationEventProps."""
        super().__init__()
        self.element_propses: list[Any] = []
        self.safe_translation: Optional[Boolean] = None
        self.secure: Optional[Boolean] = None
        self.translation: Optional[VariableDataPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SignalServiceTranslationEventProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SignalServiceTranslationEventProps":
        """Create SignalServiceTranslationEventProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SignalServiceTranslationEventProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SignalServiceTranslationEventProps since parent returns ARObject
        return cast("SignalServiceTranslationEventProps", obj)


class SignalServiceTranslationEventPropsBuilder:
    """Builder for SignalServiceTranslationEventProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SignalServiceTranslationEventProps = SignalServiceTranslationEventProps()

    def build(self) -> SignalServiceTranslationEventProps:
        """Build and return SignalServiceTranslationEventProps object.

        Returns:
            SignalServiceTranslationEventProps instance
        """
        # TODO: Add validation
        return self._obj
