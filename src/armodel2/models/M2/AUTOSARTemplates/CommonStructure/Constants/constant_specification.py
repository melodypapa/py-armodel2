"""ConstantSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 311)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 433)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import polymorphic

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class ConstantSpecification(ARElement):
    """AUTOSAR ConstantSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CONSTANT-SPECIFICATION"


    _value_spec: Optional[ValueSpecification]
    _DESERIALIZE_DISPATCH = {
        "VALUE-SPEC": ("_POLYMORPHIC", "_value_spec", ["AbstractRuleBasedValueSpecification", "ApplicationRuleBasedValueSpecification", "ApplicationValueSpecification", "ArrayValueSpecification", "CompositeRuleBasedValueSpecification", "CompositeValueSpecification", "ConstantReference", "NotAvailableValueSpecification", "NumericalValueSpecification", "RecordValueSpecification", "ReferenceValueSpecification", "TextValueSpecification"]),
    }


    def __init__(self) -> None:
        """Initialize ConstantSpecification."""
        super().__init__()
        self._value_spec: Optional[ValueSpecification] = None
    @property
    @polymorphic({"VALUE-SPEC": "ValueSpecification"})
    def value_spec(self) -> Optional[ValueSpecification]:
        """Get value_spec with polymorphic wrapper handling."""
        return self._value_spec

    @value_spec.setter
    def value_spec(self, value: Optional[ValueSpecification]) -> None:
        """Set value_spec with polymorphic wrapper handling."""
        self._value_spec = value


    def serialize(self) -> ET.Element:
        """Serialize ConstantSpecification to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConstantSpecification, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize value_spec (polymorphic wrapper "VALUE-SPEC")
        if self.value_spec is not None:
            serialized = SerializationHelper.serialize_item(self.value_spec, "ValueSpecification")
            if serialized is not None:
                # For polymorphic types, wrap the serialized element (preserving concrete type)
                wrapped = ET.Element("VALUE-SPEC")
                wrapped.append(serialized)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConstantSpecification":
        """Deserialize XML element to ConstantSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConstantSpecification object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConstantSpecification, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "VALUE-SPEC":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ABSTRACT-RULE-BASED-VALUE-SPECIFICATION":
                        setattr(obj, "_value_spec", SerializationHelper.deserialize_by_tag(child[0], "AbstractRuleBasedValueSpecification"))
                    elif concrete_tag == "APPLICATION-RULE-BASED-VALUE-SPECIFICATION":
                        setattr(obj, "_value_spec", SerializationHelper.deserialize_by_tag(child[0], "ApplicationRuleBasedValueSpecification"))
                    elif concrete_tag == "APPLICATION-VALUE-SPECIFICATION":
                        setattr(obj, "_value_spec", SerializationHelper.deserialize_by_tag(child[0], "ApplicationValueSpecification"))
                    elif concrete_tag == "ARRAY-VALUE-SPECIFICATION":
                        setattr(obj, "_value_spec", SerializationHelper.deserialize_by_tag(child[0], "ArrayValueSpecification"))
                    elif concrete_tag == "COMPOSITE-RULE-BASED-VALUE-SPECIFICATION":
                        setattr(obj, "_value_spec", SerializationHelper.deserialize_by_tag(child[0], "CompositeRuleBasedValueSpecification"))
                    elif concrete_tag == "COMPOSITE-VALUE-SPECIFICATION":
                        setattr(obj, "_value_spec", SerializationHelper.deserialize_by_tag(child[0], "CompositeValueSpecification"))
                    elif concrete_tag == "CONSTANT-REFERENCE":
                        setattr(obj, "_value_spec", SerializationHelper.deserialize_by_tag(child[0], "ConstantReference"))
                    elif concrete_tag == "NOT-AVAILABLE-VALUE-SPECIFICATION":
                        setattr(obj, "_value_spec", SerializationHelper.deserialize_by_tag(child[0], "NotAvailableValueSpecification"))
                    elif concrete_tag == "NUMERICAL-VALUE-SPECIFICATION":
                        setattr(obj, "_value_spec", SerializationHelper.deserialize_by_tag(child[0], "NumericalValueSpecification"))
                    elif concrete_tag == "RECORD-VALUE-SPECIFICATION":
                        setattr(obj, "_value_spec", SerializationHelper.deserialize_by_tag(child[0], "RecordValueSpecification"))
                    elif concrete_tag == "REFERENCE-VALUE-SPECIFICATION":
                        setattr(obj, "_value_spec", SerializationHelper.deserialize_by_tag(child[0], "ReferenceValueSpecification"))
                    elif concrete_tag == "TEXT-VALUE-SPECIFICATION":
                        setattr(obj, "_value_spec", SerializationHelper.deserialize_by_tag(child[0], "TextValueSpecification"))

        return obj



class ConstantSpecificationBuilder(ARElementBuilder):
    """Builder for ConstantSpecification with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ConstantSpecification = ConstantSpecification()


    def with_value_spec(self, value: Optional[ValueSpecification]) -> "ConstantSpecificationBuilder":
        """Set value_spec attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.value_spec = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "valueSpec",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ConstantSpecification:
        """Build and return the ConstantSpecification instance with validation."""
        self._validate_instance()
        return self._obj