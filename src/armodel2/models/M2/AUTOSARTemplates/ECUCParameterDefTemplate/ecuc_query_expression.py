"""EcucQueryExpression AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 89)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
        EcucDefinitionElement,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class EcucQueryExpression(ARObject):
    """AUTOSAR EcucQueryExpression."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECUC-QUERY-EXPRESSION"


    config_element_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "CONFIG-ELEMENT-REF": ("_POLYMORPHIC", "config_element_ref", ["EcucAddInfoParamDef", "EcucBooleanParamDef", "EcucChoiceContainerDef", "EcucChoiceReferenceDef", "EcucCommonAttributes", "EcucContainerDef", "EcucEnumerationParamDef", "EcucFloatParamDef", "EcucForeignReferenceDef", "EcucFunctionNameDef", "EcucInstanceReferenceDef", "EcucIntegerParamDef", "EcucLinkerSymbolDef", "EcucModuleDef", "EcucMultilineStringParamDef", "EcucParamConfContainerDef", "EcucReferenceDef", "EcucStringParamDef", "EcucUriReferenceDef"]),
    }


    def __init__(self) -> None:
        """Initialize EcucQueryExpression."""
        super().__init__()
        self.config_element_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucQueryExpression to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucQueryExpression, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize config_element_ref
        if self.config_element_ref is not None:
            serialized = SerializationHelper.serialize_item(self.config_element_ref, "EcucDefinitionElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONFIG-ELEMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucQueryExpression":
        """Deserialize XML element to EcucQueryExpression object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucQueryExpression object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucQueryExpression, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONFIG-ELEMENT-REF":
                setattr(obj, "config_element_ref", ARRef.deserialize(child))

        return obj



class EcucQueryExpressionBuilder(BuilderBase):
    """Builder for EcucQueryExpression with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucQueryExpression = EcucQueryExpression()


    def with_config_element(self, value: Optional[EcucDefinitionElement]) -> "EcucQueryExpressionBuilder":
        """Set config_element attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'config_element' is required and cannot be None")
        self._obj.config_element = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "configElement",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EcucQueryExpression:
        """Build and return the EcucQueryExpression instance with validation."""
        self._validate_instance()
        return self._obj