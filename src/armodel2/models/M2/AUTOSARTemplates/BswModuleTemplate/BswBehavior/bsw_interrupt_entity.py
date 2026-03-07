"""BswInterruptEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 75)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 212)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import BswModuleEntityBuilder
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import (
    BswInterruptCategory,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BswInterruptEntity(BswModuleEntity):
    """AUTOSAR BswInterruptEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BSW-INTERRUPT-ENTITY"


    interrupt_category: Optional[BswInterruptCategory]
    interrupt_source: Optional[String]
    _DESERIALIZE_DISPATCH = {
        "INTERRUPT-CATEGORY": lambda obj, elem: setattr(obj, "interrupt_category", BswInterruptCategory.deserialize(elem)),
        "INTERRUPT-SOURCE": lambda obj, elem: setattr(obj, "interrupt_source", SerializationHelper.deserialize_by_tag(elem, "String")),
    }


    def __init__(self) -> None:
        """Initialize BswInterruptEntity."""
        super().__init__()
        self.interrupt_category: Optional[BswInterruptCategory] = None
        self.interrupt_source: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize BswInterruptEntity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswInterruptEntity, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize interrupt_category
        if self.interrupt_category is not None:
            serialized = SerializationHelper.serialize_item(self.interrupt_category, "BswInterruptCategory")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTERRUPT-CATEGORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize interrupt_source
        if self.interrupt_source is not None:
            serialized = SerializationHelper.serialize_item(self.interrupt_source, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTERRUPT-SOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswInterruptEntity":
        """Deserialize XML element to BswInterruptEntity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswInterruptEntity object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswInterruptEntity, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "INTERRUPT-CATEGORY":
                setattr(obj, "interrupt_category", BswInterruptCategory.deserialize(child))
            elif tag == "INTERRUPT-SOURCE":
                setattr(obj, "interrupt_source", SerializationHelper.deserialize_by_tag(child, "String"))

        return obj



class BswInterruptEntityBuilder(BswModuleEntityBuilder):
    """Builder for BswInterruptEntity with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswInterruptEntity = BswInterruptEntity()


    def with_interrupt_category(self, value: Optional[BswInterruptCategory]) -> "BswInterruptEntityBuilder":
        """Set interrupt_category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'interrupt_category' is required and cannot be None")
        self._obj.interrupt_category = value
        return self

    def with_interrupt_source(self, value: Optional[String]) -> "BswInterruptEntityBuilder":
        """Set interrupt_source attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'interrupt_source' is required and cannot be None")
        self._obj.interrupt_source = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "interruptCategory",
        "interruptSource",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BswInterruptEntity:
        """Build and return the BswInterruptEntity instance with validation."""
        self._validate_instance()
        return self._obj