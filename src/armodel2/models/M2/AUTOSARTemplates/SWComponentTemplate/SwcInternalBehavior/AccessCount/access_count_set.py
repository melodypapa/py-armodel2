"""AccessCountSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_AccessCount.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.access_count import (
    AccessCount,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AccessCountSet(ARObject):
    """AUTOSAR AccessCountSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ACCESS-COUNT-SET"


    access_counts: list[AccessCount]
    count_profile: Optional[NameToken]
    _DESERIALIZE_DISPATCH = {
        "ACCESS-COUNTS": lambda obj, elem: obj.access_counts.append(SerializationHelper.deserialize_by_tag(elem, "AccessCount")),
        "COUNT-PROFILE": lambda obj, elem: setattr(obj, "count_profile", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
    }


    def __init__(self) -> None:
        """Initialize AccessCountSet."""
        super().__init__()
        self.access_counts: list[AccessCount] = []
        self.count_profile: Optional[NameToken] = None

    def serialize(self) -> ET.Element:
        """Serialize AccessCountSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AccessCountSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize access_counts (list to container "ACCESS-COUNTS")
        if self.access_counts:
            wrapper = ET.Element("ACCESS-COUNTS")
            for item in self.access_counts:
                serialized = SerializationHelper.serialize_item(item, "AccessCount")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize count_profile
        if self.count_profile is not None:
            serialized = SerializationHelper.serialize_item(self.count_profile, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUNT-PROFILE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AccessCountSet":
        """Deserialize XML element to AccessCountSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AccessCountSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AccessCountSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ACCESS-COUNTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.access_counts.append(SerializationHelper.deserialize_by_tag(item_elem, "AccessCount"))
            elif tag == "COUNT-PROFILE":
                setattr(obj, "count_profile", SerializationHelper.deserialize_by_tag(child, "NameToken"))

        return obj



class AccessCountSetBuilder(BuilderBase):
    """Builder for AccessCountSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AccessCountSet = AccessCountSet()


    def with_access_counts(self, items: list[AccessCount]) -> "AccessCountSetBuilder":
        """Set access_counts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.access_counts = list(items) if items else []
        return self

    def with_count_profile(self, value: Optional[NameToken]) -> "AccessCountSetBuilder":
        """Set count_profile attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'count_profile' is required and cannot be None")
        self._obj.count_profile = value
        return self


    def add_access_count(self, item: AccessCount) -> "AccessCountSetBuilder":
        """Add a single item to access_counts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.access_counts.append(item)
        return self

    def clear_access_counts(self) -> "AccessCountSetBuilder":
        """Clear all items from access_counts list.

        Returns:
            self for method chaining
        """
        self._obj.access_counts = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "accessCount",
        "countProfile",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> AccessCountSet:
        """Build and return the AccessCountSet instance with validation."""
        self._validate_instance()
        return self._obj