"""BswExclusiveAreaPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 82)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
    ApiPrincipleEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BswExclusiveAreaPolicy(ARObject):
    """AUTOSAR BswExclusiveAreaPolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BSW-EXCLUSIVE-AREA-POLICY"


    api_principle: Optional[ApiPrincipleEnum]
    exclusive_area_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "API-PRINCIPLE": lambda obj, elem: setattr(obj, "api_principle", ApiPrincipleEnum.deserialize(elem)),
        "EXCLUSIVE-AREA-REF": lambda obj, elem: setattr(obj, "exclusive_area_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize BswExclusiveAreaPolicy."""
        super().__init__()
        self.api_principle: Optional[ApiPrincipleEnum] = None
        self.exclusive_area_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize BswExclusiveAreaPolicy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswExclusiveAreaPolicy, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize api_principle
        if self.api_principle is not None:
            serialized = SerializationHelper.serialize_item(self.api_principle, "ApiPrincipleEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("API-PRINCIPLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize exclusive_area_ref
        if self.exclusive_area_ref is not None:
            serialized = SerializationHelper.serialize_item(self.exclusive_area_ref, "ExclusiveArea")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXCLUSIVE-AREA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswExclusiveAreaPolicy":
        """Deserialize XML element to BswExclusiveAreaPolicy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswExclusiveAreaPolicy object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswExclusiveAreaPolicy, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "API-PRINCIPLE":
                setattr(obj, "api_principle", ApiPrincipleEnum.deserialize(child))
            elif tag == "EXCLUSIVE-AREA-REF":
                setattr(obj, "exclusive_area_ref", ARRef.deserialize(child))

        return obj



class BswExclusiveAreaPolicyBuilder(BuilderBase):
    """Builder for BswExclusiveAreaPolicy with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswExclusiveAreaPolicy = BswExclusiveAreaPolicy()


    def with_api_principle(self, value: Optional[ApiPrincipleEnum]) -> "BswExclusiveAreaPolicyBuilder":
        """Set api_principle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.api_principle = value
        return self

    def with_exclusive_area(self, value: Optional[ExclusiveArea]) -> "BswExclusiveAreaPolicyBuilder":
        """Set exclusive_area attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.exclusive_area = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "apiPrinciple",
        "exclusiveArea",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BswExclusiveAreaPolicy:
        """Build and return the BswExclusiveAreaPolicy instance with validation."""
        self._validate_instance()
        return self._obj