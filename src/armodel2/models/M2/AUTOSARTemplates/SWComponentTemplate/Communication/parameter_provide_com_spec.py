"""ParameterProvideComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 192)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import polymorphic

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import PPortComSpecBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class ParameterProvideComSpec(PPortComSpec):
    """AUTOSAR ParameterProvideComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PARAMETER-PROVIDE-COM-SPEC"


    _init_value: Optional[ValueSpecification]
    parameter_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "INIT-VALUE": ("_POLYMORPHIC", "_init_value", ["AbstractRuleBasedValueSpecification", "ApplicationRuleBasedValueSpecification", "ApplicationValueSpecification", "ArrayValueSpecification", "CompositeRuleBasedValueSpecification", "CompositeValueSpecification", "ConstantReference", "NotAvailableValueSpecification", "NumericalValueSpecification", "RecordValueSpecification", "ReferenceValueSpecification", "TextValueSpecification"]),
        "PARAMETER-REF": lambda obj, elem: setattr(obj, "parameter_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ParameterProvideComSpec."""
        super().__init__()
        self._init_value: Optional[ValueSpecification] = None
        self.parameter_ref: Optional[ARRef] = None
    @property
    @polymorphic({"INIT-VALUE": "ValueSpecification"})
    def init_value(self) -> Optional[ValueSpecification]:
        """Get init_value with polymorphic wrapper handling."""
        return self._init_value

    @init_value.setter
    def init_value(self, value: Optional[ValueSpecification]) -> None:
        """Set init_value with polymorphic wrapper handling."""
        self._init_value = value


    def serialize(self) -> ET.Element:
        """Serialize ParameterProvideComSpec to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ParameterProvideComSpec, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize init_value (polymorphic wrapper "INIT-VALUE")
        if self.init_value is not None:
            serialized = SerializationHelper.serialize_item(self.init_value, "ValueSpecification")
            if serialized is not None:
                # For polymorphic types, wrap the serialized element (preserving concrete type)
                wrapped = ET.Element("INIT-VALUE")
                wrapped.append(serialized)
                elem.append(wrapped)

        # Serialize parameter_ref
        if self.parameter_ref is not None:
            serialized = SerializationHelper.serialize_item(self.parameter_ref, "ParameterDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PARAMETER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ParameterProvideComSpec":
        """Deserialize XML element to ParameterProvideComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ParameterProvideComSpec object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ParameterProvideComSpec, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "INIT-VALUE":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ABSTRACT-RULE-BASED-VALUE-SPECIFICATION":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "AbstractRuleBasedValueSpecification"))
                    elif concrete_tag == "APPLICATION-RULE-BASED-VALUE-SPECIFICATION":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "ApplicationRuleBasedValueSpecification"))
                    elif concrete_tag == "APPLICATION-VALUE-SPECIFICATION":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "ApplicationValueSpecification"))
                    elif concrete_tag == "ARRAY-VALUE-SPECIFICATION":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "ArrayValueSpecification"))
                    elif concrete_tag == "COMPOSITE-RULE-BASED-VALUE-SPECIFICATION":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "CompositeRuleBasedValueSpecification"))
                    elif concrete_tag == "COMPOSITE-VALUE-SPECIFICATION":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "CompositeValueSpecification"))
                    elif concrete_tag == "CONSTANT-REFERENCE":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "ConstantReference"))
                    elif concrete_tag == "NOT-AVAILABLE-VALUE-SPECIFICATION":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "NotAvailableValueSpecification"))
                    elif concrete_tag == "NUMERICAL-VALUE-SPECIFICATION":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "NumericalValueSpecification"))
                    elif concrete_tag == "RECORD-VALUE-SPECIFICATION":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "RecordValueSpecification"))
                    elif concrete_tag == "REFERENCE-VALUE-SPECIFICATION":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "ReferenceValueSpecification"))
                    elif concrete_tag == "TEXT-VALUE-SPECIFICATION":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "TextValueSpecification"))
            elif tag == "PARAMETER-REF":
                setattr(obj, "parameter_ref", ARRef.deserialize(child))

        return obj



class ParameterProvideComSpecBuilder(PPortComSpecBuilder):
    """Builder for ParameterProvideComSpec with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ParameterProvideComSpec = ParameterProvideComSpec()


    def with_init_value(self, value: Optional[ValueSpecification]) -> "ParameterProvideComSpecBuilder":
        """Set init_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'init_value' is required and cannot be None")
        self._obj.init_value = value
        return self

    def with_parameter(self, value: Optional[ParameterDataPrototype]) -> "ParameterProvideComSpecBuilder":
        """Set parameter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'parameter' is required and cannot be None")
        self._obj.parameter = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "initValue",
        "parameter",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ParameterProvideComSpec:
        """Build and return the ParameterProvideComSpec instance with validation."""
        self._validate_instance()
        return self._obj