"""SignalServiceTranslationPropsSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)


class SignalServiceTranslationPropsSet(ARElement):
    """AUTOSAR SignalServiceTranslationPropsSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("signal_service_propses", None, False, True, any (SignalService)),  # signalServicePropses
    ]

    def __init__(self) -> None:
        """Initialize SignalServiceTranslationPropsSet."""
        super().__init__()
        self.signal_service_propses: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SignalServiceTranslationPropsSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SignalServiceTranslationPropsSet":
        """Create SignalServiceTranslationPropsSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SignalServiceTranslationPropsSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SignalServiceTranslationPropsSet since parent returns ARObject
        return cast("SignalServiceTranslationPropsSet", obj)


class SignalServiceTranslationPropsSetBuilder:
    """Builder for SignalServiceTranslationPropsSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SignalServiceTranslationPropsSet = SignalServiceTranslationPropsSet()

    def build(self) -> SignalServiceTranslationPropsSet:
        """Build and return SignalServiceTranslationPropsSet object.

        Returns:
            SignalServiceTranslationPropsSet instance
        """
        # TODO: Add validation
        return self._obj
