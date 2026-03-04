"""BswEntryRelationship AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 51)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 52)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BswEntryRelationship(ARObject):
    """AUTOSAR BswEntryRelationship."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BSW-ENTRY-RELATIONSHIP"


    bsw_entry: Optional[BswEntryRelationship]
    from_ref: Optional[ARRef]
    to_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "BSW-ENTRY": lambda obj, elem: setattr(obj, "bsw_entry", SerializationHelper.deserialize_by_tag(elem, "BswEntryRelationship")),
        "FROM-REF": lambda obj, elem: setattr(obj, "from_ref", ARRef.deserialize(elem)),
        "TO-REF": lambda obj, elem: setattr(obj, "to_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize BswEntryRelationship."""
        super().__init__()
        self.bsw_entry: Optional[BswEntryRelationship] = None
        self.from_ref: Optional[ARRef] = None
        self.to_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize BswEntryRelationship to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswEntryRelationship, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bsw_entry
        if self.bsw_entry is not None:
            serialized = SerializationHelper.serialize_item(self.bsw_entry, "BswEntryRelationship")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-ENTRY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize from_ref
        if self.from_ref is not None:
            serialized = SerializationHelper.serialize_item(self.from_ref, "BswModuleEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FROM-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize to_ref
        if self.to_ref is not None:
            serialized = SerializationHelper.serialize_item(self.to_ref, "BswModuleEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TO-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswEntryRelationship":
        """Deserialize XML element to BswEntryRelationship object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswEntryRelationship object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswEntryRelationship, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BSW-ENTRY":
                setattr(obj, "bsw_entry", SerializationHelper.deserialize_by_tag(child, "BswEntryRelationship"))
            elif tag == "FROM-REF":
                setattr(obj, "from_ref", ARRef.deserialize(child))
            elif tag == "TO-REF":
                setattr(obj, "to_ref", ARRef.deserialize(child))

        return obj



class BswEntryRelationshipBuilder(BuilderBase):
    """Builder for BswEntryRelationship with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswEntryRelationship = BswEntryRelationship()


    def with_bsw_entry(self, value: Optional[BswEntryRelationship]) -> "BswEntryRelationshipBuilder":
        """Set bsw_entry attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bsw_entry = value
        return self

    def with_from(self, value: Optional[BswModuleEntry]) -> "BswEntryRelationshipBuilder":
        """Set from attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        setattr(self._obj, 'from', value)
        return self

    def with_to(self, value: Optional[BswModuleEntry]) -> "BswEntryRelationshipBuilder":
        """Set to attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.to = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "bswEntry",
        "from",
        "to",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BswEntryRelationship:
        """Build and return the BswEntryRelationship instance with validation."""
        self._validate_instance()
        return self._obj