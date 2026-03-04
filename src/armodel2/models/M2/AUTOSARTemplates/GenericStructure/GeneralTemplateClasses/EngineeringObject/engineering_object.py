"""EngineeringObject AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 132)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_EngineeringObject.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    RevisionLabelString,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EngineeringObject(ARObject, ABC):
    """AUTOSAR EngineeringObject."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    short_label: NameToken
    category: NameToken
    domain: Optional[NameToken]
    revision_labels: list[RevisionLabelString]
    _DESERIALIZE_DISPATCH = {
        "SHORT-LABEL": lambda obj, elem: setattr(obj, "short_label", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
        "CATEGORY": lambda obj, elem: setattr(obj, "category", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
        "DOMAIN": lambda obj, elem: setattr(obj, "domain", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
        "REVISION-LABELS": lambda obj, elem: obj.revision_labels.append(SerializationHelper.deserialize_by_tag(elem, "RevisionLabelString")),
    }


    def __init__(self) -> None:
        """Initialize EngineeringObject."""
        super().__init__()
        self.short_label: NameToken = None
        self.category: NameToken = None
        self.domain: Optional[NameToken] = None
        self.revision_labels: list[RevisionLabelString] = []

    def serialize(self) -> ET.Element:
        """Serialize EngineeringObject to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EngineeringObject, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize short_label
        if self.short_label is not None:
            serialized = SerializationHelper.serialize_item(self.short_label, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize category
        if self.category is not None:
            serialized = SerializationHelper.serialize_item(self.category, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CATEGORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize domain
        if self.domain is not None:
            serialized = SerializationHelper.serialize_item(self.domain, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DOMAIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize revision_labels (list to container "REVISION-LABELS")
        if self.revision_labels:
            wrapper = ET.Element("REVISION-LABELS")
            for item in self.revision_labels:
                serialized = SerializationHelper.serialize_item(item, "RevisionLabelString")
                if serialized is not None:
                    child_elem = ET.Element("REVISION-LABEL")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EngineeringObject":
        """Deserialize XML element to EngineeringObject object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EngineeringObject object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EngineeringObject, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SHORT-LABEL":
                setattr(obj, "short_label", SerializationHelper.deserialize_by_tag(child, "NameToken"))
            elif tag == "CATEGORY":
                setattr(obj, "category", SerializationHelper.deserialize_by_tag(child, "NameToken"))
            elif tag == "DOMAIN":
                setattr(obj, "domain", SerializationHelper.deserialize_by_tag(child, "NameToken"))
            elif tag == "REVISION-LABELS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.revision_labels.append(SerializationHelper.deserialize_by_tag(item_elem, "RevisionLabelString"))

        return obj



class EngineeringObjectBuilder(BuilderBase, ABC):
    """Builder for EngineeringObject with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EngineeringObject = EngineeringObject()


    def with_short_label(self, value: NameToken) -> "EngineeringObjectBuilder":
        """Set short_label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_label = value
        return self

    def with_category(self, value: NameToken) -> "EngineeringObjectBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_domain(self, value: Optional[NameToken]) -> "EngineeringObjectBuilder":
        """Set domain attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.domain = value
        return self

    def with_revision_labels(self, items: list[RevisionLabelString]) -> "EngineeringObjectBuilder":
        """Set revision_labels list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.revision_labels = list(items) if items else []
        return self


    def add_revision_label(self, item: RevisionLabelString) -> "EngineeringObjectBuilder":
        """Add a single item to revision_labels list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.revision_labels.append(item)
        return self

    def clear_revision_labels(self) -> "EngineeringObjectBuilder":
        """Clear all items from revision_labels list.

        Returns:
            self for method chaining
        """
        self._obj.revision_labels = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "category",
        "shortLabel",
    }
    _OPTIONAL_ATTRIBUTES = {
        "domain",
        "revisionLabel",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "category", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'category' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'category' is None", UserWarning)
        if getattr(self._obj, "shortLabel", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'shortLabel' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'shortLabel' is None", UserWarning)


    @abstractmethod
    def build(self) -> EngineeringObject:
        """Build and return the EngineeringObject instance (abstract)."""
        raise NotImplementedError