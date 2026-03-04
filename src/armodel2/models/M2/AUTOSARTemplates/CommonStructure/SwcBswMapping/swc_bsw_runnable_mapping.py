"""SwcBswRunnableMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 110)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SwcBswMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
    RunnableEntity,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwcBswRunnableMapping(ARObject):
    """AUTOSAR SwcBswRunnableMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SWC-BSW-RUNNABLE-MAPPING"


    bsw_entity_ref: Optional[ARRef]
    swc_runnable_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "BSW-ENTITY-REF": ("_POLYMORPHIC", "bsw_entity_ref", ["BswCalledEntity", "BswInterruptEntity", "BswSchedulableEntity"]),
        "SWC-RUNNABLE-REF": lambda obj, elem: setattr(obj, "swc_runnable_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize SwcBswRunnableMapping."""
        super().__init__()
        self.bsw_entity_ref: Optional[ARRef] = None
        self.swc_runnable_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SwcBswRunnableMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcBswRunnableMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bsw_entity_ref
        if self.bsw_entity_ref is not None:
            serialized = SerializationHelper.serialize_item(self.bsw_entity_ref, "BswModuleEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-ENTITY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize swc_runnable_ref
        if self.swc_runnable_ref is not None:
            serialized = SerializationHelper.serialize_item(self.swc_runnable_ref, "RunnableEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SWC-RUNNABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcBswRunnableMapping":
        """Deserialize XML element to SwcBswRunnableMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcBswRunnableMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcBswRunnableMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BSW-ENTITY-REF":
                setattr(obj, "bsw_entity_ref", ARRef.deserialize(child))
            elif tag == "SWC-RUNNABLE-REF":
                setattr(obj, "swc_runnable_ref", ARRef.deserialize(child))

        return obj



class SwcBswRunnableMappingBuilder(BuilderBase):
    """Builder for SwcBswRunnableMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwcBswRunnableMapping = SwcBswRunnableMapping()


    def with_bsw_entity(self, value: Optional[BswModuleEntity]) -> "SwcBswRunnableMappingBuilder":
        """Set bsw_entity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bsw_entity = value
        return self

    def with_swc_runnable(self, value: Optional[RunnableEntity]) -> "SwcBswRunnableMappingBuilder":
        """Set swc_runnable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.swc_runnable = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "bswEntity",
        "swcRunnable",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SwcBswRunnableMapping:
        """Build and return the SwcBswRunnableMapping instance with validation."""
        self._validate_instance()
        return self._obj