"""SignalServiceTranslationPropsSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 730)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SignalServiceTranslation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SignalServiceTranslationPropsSet(ARElement):
    """AUTOSAR SignalServiceTranslationPropsSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SIGNAL-SERVICE-TRANSLATION-PROPS-SET"


    signal_service_propses: list[Any]
    _DESERIALIZE_DISPATCH = {
        "SIGNAL-SERVICE-PROPSS": lambda obj, elem: obj.signal_service_propses.append(SerializationHelper.deserialize_by_tag(elem, "any (SignalService)")),
    }


    def __init__(self) -> None:
        """Initialize SignalServiceTranslationPropsSet."""
        super().__init__()
        self.signal_service_propses: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize SignalServiceTranslationPropsSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SignalServiceTranslationPropsSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize signal_service_propses (list to container "SIGNAL-SERVICE-PROPSS")
        if self.signal_service_propses:
            wrapper = ET.Element("SIGNAL-SERVICE-PROPSS")
            for item in self.signal_service_propses:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SignalServiceTranslationPropsSet":
        """Deserialize XML element to SignalServiceTranslationPropsSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SignalServiceTranslationPropsSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SignalServiceTranslationPropsSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SIGNAL-SERVICE-PROPSS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.signal_service_propses.append(SerializationHelper.deserialize_by_tag(item_elem, "any (SignalService)"))

        return obj



class SignalServiceTranslationPropsSetBuilder(ARElementBuilder):
    """Builder for SignalServiceTranslationPropsSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SignalServiceTranslationPropsSet = SignalServiceTranslationPropsSet()


    def with_signal_service_propses(self, items: list[Any]) -> "SignalServiceTranslationPropsSetBuilder":
        """Set signal_service_propses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.signal_service_propses = list(items) if items else []
        return self


    def add_signal_service_props(self, item: Any) -> "SignalServiceTranslationPropsSetBuilder":
        """Add a single item to signal_service_propses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.signal_service_propses.append(item)
        return self

    def clear_signal_service_propses(self) -> "SignalServiceTranslationPropsSetBuilder":
        """Clear all items from signal_service_propses list.

        Returns:
            self for method chaining
        """
        self._obj.signal_service_propses = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "signalServiceProps",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SignalServiceTranslationPropsSet:
        """Build and return the SignalServiceTranslationPropsSet instance with validation."""
        self._validate_instance()
        return self._obj