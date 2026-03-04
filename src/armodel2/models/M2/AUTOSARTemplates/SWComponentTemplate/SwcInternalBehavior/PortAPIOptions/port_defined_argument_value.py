"""PortDefinedArgumentValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 326)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 593)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 199)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_PortAPIOptions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import polymorphic

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.implementation_data_type import (
        ImplementationDataType,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class PortDefinedArgumentValue(ARObject):
    """AUTOSAR PortDefinedArgumentValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PORT-DEFINED-ARGUMENT-VALUE"


    _value: Optional[ValueSpecification]
    value_type_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "VALUE": ("_POLYMORPHIC", "_value", ["AbstractRuleBasedValueSpecification", "ApplicationRuleBasedValueSpecification", "ApplicationValueSpecification", "ArrayValueSpecification", "CompositeRuleBasedValueSpecification", "CompositeValueSpecification", "ConstantReference", "NotAvailableValueSpecification", "NumericalValueSpecification", "RecordValueSpecification", "ReferenceValueSpecification", "TextValueSpecification"]),
        "VALUE-TYPE-TREF": lambda obj, elem: setattr(obj, "value_type_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize PortDefinedArgumentValue."""
        super().__init__()
        self._value: Optional[ValueSpecification] = None
        self.value_type_ref: Optional[ARRef] = None
    @property
    @polymorphic({"VALUE": "ValueSpecification"})
    def value(self) -> Optional[ValueSpecification]:
        """Get value with polymorphic wrapper handling."""
        return self._value

    @value.setter
    def value(self, value: Optional[ValueSpecification]) -> None:
        """Set value with polymorphic wrapper handling."""
        self._value = value


    def serialize(self) -> ET.Element:
        """Serialize PortDefinedArgumentValue to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PortDefinedArgumentValue, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize value (polymorphic wrapper "VALUE")
        if self.value is not None:
            serialized = SerializationHelper.serialize_item(self.value, "ValueSpecification")
            if serialized is not None:
                # For polymorphic types, wrap the serialized element (preserving concrete type)
                wrapped = ET.Element("VALUE")
                wrapped.append(serialized)
                elem.append(wrapped)

        # Serialize value_type_ref
        if self.value_type_ref is not None:
            serialized = SerializationHelper.serialize_item(self.value_type_ref, "ImplementationDataType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALUE-TYPE-TREF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortDefinedArgumentValue":
        """Deserialize XML element to PortDefinedArgumentValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PortDefinedArgumentValue object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PortDefinedArgumentValue, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "VALUE":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ABSTRACT-RULE-BASED-VALUE-SPECIFICATION":
                        setattr(obj, "_value", SerializationHelper.deserialize_by_tag(child[0], "AbstractRuleBasedValueSpecification"))
                    elif concrete_tag == "APPLICATION-RULE-BASED-VALUE-SPECIFICATION":
                        setattr(obj, "_value", SerializationHelper.deserialize_by_tag(child[0], "ApplicationRuleBasedValueSpecification"))
                    elif concrete_tag == "APPLICATION-VALUE-SPECIFICATION":
                        setattr(obj, "_value", SerializationHelper.deserialize_by_tag(child[0], "ApplicationValueSpecification"))
                    elif concrete_tag == "ARRAY-VALUE-SPECIFICATION":
                        setattr(obj, "_value", SerializationHelper.deserialize_by_tag(child[0], "ArrayValueSpecification"))
                    elif concrete_tag == "COMPOSITE-RULE-BASED-VALUE-SPECIFICATION":
                        setattr(obj, "_value", SerializationHelper.deserialize_by_tag(child[0], "CompositeRuleBasedValueSpecification"))
                    elif concrete_tag == "COMPOSITE-VALUE-SPECIFICATION":
                        setattr(obj, "_value", SerializationHelper.deserialize_by_tag(child[0], "CompositeValueSpecification"))
                    elif concrete_tag == "CONSTANT-REFERENCE":
                        setattr(obj, "_value", SerializationHelper.deserialize_by_tag(child[0], "ConstantReference"))
                    elif concrete_tag == "NOT-AVAILABLE-VALUE-SPECIFICATION":
                        setattr(obj, "_value", SerializationHelper.deserialize_by_tag(child[0], "NotAvailableValueSpecification"))
                    elif concrete_tag == "NUMERICAL-VALUE-SPECIFICATION":
                        setattr(obj, "_value", SerializationHelper.deserialize_by_tag(child[0], "NumericalValueSpecification"))
                    elif concrete_tag == "RECORD-VALUE-SPECIFICATION":
                        setattr(obj, "_value", SerializationHelper.deserialize_by_tag(child[0], "RecordValueSpecification"))
                    elif concrete_tag == "REFERENCE-VALUE-SPECIFICATION":
                        setattr(obj, "_value", SerializationHelper.deserialize_by_tag(child[0], "ReferenceValueSpecification"))
                    elif concrete_tag == "TEXT-VALUE-SPECIFICATION":
                        setattr(obj, "_value", SerializationHelper.deserialize_by_tag(child[0], "TextValueSpecification"))
            elif tag == "VALUE-TYPE-TREF":
                setattr(obj, "value_type_ref", ARRef.deserialize(child))

        return obj



class PortDefinedArgumentValueBuilder(BuilderBase):
    """Builder for PortDefinedArgumentValue with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PortDefinedArgumentValue = PortDefinedArgumentValue()


    def with_value(self, value: Optional[ValueSpecification]) -> "PortDefinedArgumentValueBuilder":
        """Set value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.value = value
        return self

    def with_value_type(self, value: Optional[ImplementationDataType]) -> "PortDefinedArgumentValueBuilder":
        """Set value_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.value_type = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "value",
        "valueType",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> PortDefinedArgumentValue:
        """Build and return the PortDefinedArgumentValue instance with validation."""
        self._validate_instance()
        return self._obj