"""EcucParameterDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 57)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 188)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_common_attributes import (
    EcucCommonAttributes,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_common_attributes import EcucCommonAttributesBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_derivation_specification import (
    EcucDerivationSpecification,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucParameterDef(EcucCommonAttributes, ABC):
    """AUTOSAR EcucParameterDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    derivation: Optional[EcucDerivationSpecification]
    symbolic_name: Optional[Boolean]
    with_auto: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "DERIVATION": lambda obj, elem: setattr(obj, "derivation", SerializationHelper.deserialize_by_tag(elem, "EcucDerivationSpecification")),
        "SYMBOLIC-NAME": lambda obj, elem: setattr(obj, "symbolic_name", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "WITH-AUTO": lambda obj, elem: setattr(obj, "with_auto", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize EcucParameterDef."""
        super().__init__()
        self.derivation: Optional[EcucDerivationSpecification] = None
        self.symbolic_name: Optional[Boolean] = None
        self.with_auto: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucParameterDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucParameterDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize derivation
        if self.derivation is not None:
            serialized = SerializationHelper.serialize_item(self.derivation, "EcucDerivationSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DERIVATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize symbolic_name
        if self.symbolic_name is not None:
            serialized = SerializationHelper.serialize_item(self.symbolic_name, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYMBOLIC-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize with_auto
        if self.with_auto is not None:
            serialized = SerializationHelper.serialize_item(self.with_auto, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WITH-AUTO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucParameterDef":
        """Deserialize XML element to EcucParameterDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucParameterDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucParameterDef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DERIVATION":
                setattr(obj, "derivation", SerializationHelper.deserialize_by_tag(child, "EcucDerivationSpecification"))
            elif tag == "SYMBOLIC-NAME":
                setattr(obj, "symbolic_name", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "WITH-AUTO":
                setattr(obj, "with_auto", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class EcucParameterDefBuilder(EcucCommonAttributesBuilder):
    """Builder for EcucParameterDef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucParameterDef = EcucParameterDef()


    def with_derivation(self, value: Optional[EcucDerivationSpecification]) -> "EcucParameterDefBuilder":
        """Set derivation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'derivation' is required and cannot be None")
        self._obj.derivation = value
        return self

    def with_symbolic_name(self, value: Optional[Boolean]) -> "EcucParameterDefBuilder":
        """Set symbolic_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'symbolic_name' is required and cannot be None")
        self._obj.symbolic_name = value
        return self

    def with_with_auto(self, value: Optional[Boolean]) -> "EcucParameterDefBuilder":
        """Set with_auto attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'with_auto' is required and cannot be None")
        self._obj.with_auto = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "derivation",
        "symbolicName",
        "withAuto",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> EcucParameterDef:
        """Build and return the EcucParameterDef instance (abstract)."""
        raise NotImplementedError