"""SecureCommunicationPropsSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 370)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import FibexElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SecureCommunicationPropsSet(FibexElement):
    """AUTOSAR SecureCommunicationPropsSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SECURE-COMMUNICATION-PROPS-SET"


    authentications: list[Any]
    freshness_propses: list[Any]
    _DESERIALIZE_DISPATCH = {
        "AUTHENTICATIONS": lambda obj, elem: obj.authentications.append(SerializationHelper.deserialize_by_tag(elem, "any (SecureCommunication)")),
        "FRESHNESS-PROPSS": lambda obj, elem: obj.freshness_propses.append(SerializationHelper.deserialize_by_tag(elem, "any (SecureCommunication)")),
    }


    def __init__(self) -> None:
        """Initialize SecureCommunicationPropsSet."""
        super().__init__()
        self.authentications: list[Any] = []
        self.freshness_propses: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize SecureCommunicationPropsSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecureCommunicationPropsSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize authentications (list to container "AUTHENTICATIONS")
        if self.authentications:
            wrapper = ET.Element("AUTHENTICATIONS")
            for item in self.authentications:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize freshness_propses (list to container "FRESHNESS-PROPSS")
        if self.freshness_propses:
            wrapper = ET.Element("FRESHNESS-PROPSS")
            for item in self.freshness_propses:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecureCommunicationPropsSet":
        """Deserialize XML element to SecureCommunicationPropsSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecureCommunicationPropsSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecureCommunicationPropsSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "AUTHENTICATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.authentications.append(SerializationHelper.deserialize_by_tag(item_elem, "any (SecureCommunication)"))
            elif tag == "FRESHNESS-PROPSS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.freshness_propses.append(SerializationHelper.deserialize_by_tag(item_elem, "any (SecureCommunication)"))

        return obj



class SecureCommunicationPropsSetBuilder(FibexElementBuilder):
    """Builder for SecureCommunicationPropsSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SecureCommunicationPropsSet = SecureCommunicationPropsSet()


    def with_authentications(self, items: list[Any]) -> "SecureCommunicationPropsSetBuilder":
        """Set authentications list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.authentications = list(items) if items else []
        return self

    def with_freshness_propses(self, items: list[Any]) -> "SecureCommunicationPropsSetBuilder":
        """Set freshness_propses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.freshness_propses = list(items) if items else []
        return self


    def add_authentication(self, item: Any) -> "SecureCommunicationPropsSetBuilder":
        """Add a single item to authentications list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.authentications.append(item)
        return self

    def clear_authentications(self) -> "SecureCommunicationPropsSetBuilder":
        """Clear all items from authentications list.

        Returns:
            self for method chaining
        """
        self._obj.authentications = []
        return self

    def add_freshness_props(self, item: Any) -> "SecureCommunicationPropsSetBuilder":
        """Add a single item to freshness_propses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.freshness_propses.append(item)
        return self

    def clear_freshness_propses(self) -> "SecureCommunicationPropsSetBuilder":
        """Clear all items from freshness_propses list.

        Returns:
            self for method chaining
        """
        self._obj.freshness_propses = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "authentication",
        "freshnessProps",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SecureCommunicationPropsSet:
        """Build and return the SecureCommunicationPropsSet instance with validation."""
        self._validate_instance()
        return self._obj