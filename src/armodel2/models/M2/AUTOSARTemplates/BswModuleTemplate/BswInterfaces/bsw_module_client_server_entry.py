"""BswModuleClientServerEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 53)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import ReferrableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BswModuleClientServerEntry(Referrable):
    """AUTOSAR BswModuleClientServerEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BSW-MODULE-CLIENT-SERVER-ENTRY"


    encapsulated_entry_ref: Optional[ARRef]
    is_reentrant: Optional[Boolean]
    is_synchronous: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "ENCAPSULATED-ENTRY-REF": lambda obj, elem: setattr(obj, "encapsulated_entry_ref", ARRef.deserialize(elem)),
        "IS-REENTRANT": lambda obj, elem: setattr(obj, "is_reentrant", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "IS-SYNCHRONOUS": lambda obj, elem: setattr(obj, "is_synchronous", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize BswModuleClientServerEntry."""
        super().__init__()
        self.encapsulated_entry_ref: Optional[ARRef] = None
        self.is_reentrant: Optional[Boolean] = None
        self.is_synchronous: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize BswModuleClientServerEntry to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswModuleClientServerEntry, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize encapsulated_entry_ref
        if self.encapsulated_entry_ref is not None:
            serialized = SerializationHelper.serialize_item(self.encapsulated_entry_ref, "BswModuleEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENCAPSULATED-ENTRY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_reentrant
        if self.is_reentrant is not None:
            serialized = SerializationHelper.serialize_item(self.is_reentrant, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-REENTRANT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_synchronous
        if self.is_synchronous is not None:
            serialized = SerializationHelper.serialize_item(self.is_synchronous, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-SYNCHRONOUS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModuleClientServerEntry":
        """Deserialize XML element to BswModuleClientServerEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswModuleClientServerEntry object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswModuleClientServerEntry, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ENCAPSULATED-ENTRY-REF":
                setattr(obj, "encapsulated_entry_ref", ARRef.deserialize(child))
            elif tag == "IS-REENTRANT":
                setattr(obj, "is_reentrant", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "IS-SYNCHRONOUS":
                setattr(obj, "is_synchronous", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class BswModuleClientServerEntryBuilder(ReferrableBuilder):
    """Builder for BswModuleClientServerEntry with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswModuleClientServerEntry = BswModuleClientServerEntry()


    def with_encapsulated_entry(self, value: Optional[BswModuleEntry]) -> "BswModuleClientServerEntryBuilder":
        """Set encapsulated_entry attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'encapsulated_entry' is required and cannot be None")
        self._obj.encapsulated_entry = value
        return self

    def with_is_reentrant(self, value: Optional[Boolean]) -> "BswModuleClientServerEntryBuilder":
        """Set is_reentrant attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'is_reentrant' is required and cannot be None")
        self._obj.is_reentrant = value
        return self

    def with_is_synchronous(self, value: Optional[Boolean]) -> "BswModuleClientServerEntryBuilder":
        """Set is_synchronous attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'is_synchronous' is required and cannot be None")
        self._obj.is_synchronous = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "encapsulatedEntry",
        "isReentrant",
        "isSynchronous",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BswModuleClientServerEntry:
        """Build and return the BswModuleClientServerEntry instance with validation."""
        self._validate_instance()
        return self._obj