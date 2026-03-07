"""ConstantReference AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 440)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import ValueSpecificationBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification import (
    ConstantSpecification,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ConstantReference(ValueSpecification):
    """AUTOSAR ConstantReference."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CONSTANT-REFERENCE"


    constant_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "CONSTANT-REF": lambda obj, elem: setattr(obj, "constant_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ConstantReference."""
        super().__init__()
        self.constant_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ConstantReference to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConstantReference, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize constant_ref
        if self.constant_ref is not None:
            serialized = SerializationHelper.serialize_item(self.constant_ref, "ConstantSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONSTANT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConstantReference":
        """Deserialize XML element to ConstantReference object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConstantReference object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConstantReference, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONSTANT-REF":
                setattr(obj, "constant_ref", ARRef.deserialize(child))

        return obj



class ConstantReferenceBuilder(ValueSpecificationBuilder):
    """Builder for ConstantReference with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ConstantReference = ConstantReference()


    def with_constant(self, value: Optional[ConstantSpecification]) -> "ConstantReferenceBuilder":
        """Set constant attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'constant' is required and cannot be None")
        self._obj.constant = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "constant",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ConstantReference:
        """Build and return the ConstantReference instance with validation."""
        self._validate_instance()
        return self._obj