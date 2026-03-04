"""SignalServiceTranslationElementProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 735)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SignalServiceTranslation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Filter.data_filter import (
    DataFilter,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SignalServiceTranslationElementProps(Identifiable):
    """AUTOSAR SignalServiceTranslationElementProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SIGNAL-SERVICE-TRANSLATION-ELEMENT-PROPS"


    element_ref: Optional[ARRef]
    filter: Optional[DataFilter]
    transmission: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "ELEMENT-REF": ("_POLYMORPHIC", "element_ref", ["ApplicationArrayElement", "ApplicationCompositeElementDataPrototype", "ApplicationRecordElement", "ArgumentDataPrototype", "AutosarDataPrototype", "ParameterDataPrototype", "VariableDataPrototype"]),
        "FILTER": lambda obj, elem: setattr(obj, "filter", SerializationHelper.deserialize_by_tag(elem, "DataFilter")),
        "TRANSMISSION": lambda obj, elem: setattr(obj, "transmission", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize SignalServiceTranslationElementProps."""
        super().__init__()
        self.element_ref: Optional[ARRef] = None
        self.filter: Optional[DataFilter] = None
        self.transmission: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize SignalServiceTranslationElementProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SignalServiceTranslationElementProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize element_ref
        if self.element_ref is not None:
            serialized = SerializationHelper.serialize_item(self.element_ref, "DataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ELEMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize filter
        if self.filter is not None:
            serialized = SerializationHelper.serialize_item(self.filter, "DataFilter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transmission
        if self.transmission is not None:
            serialized = SerializationHelper.serialize_item(self.transmission, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSMISSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SignalServiceTranslationElementProps":
        """Deserialize XML element to SignalServiceTranslationElementProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SignalServiceTranslationElementProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SignalServiceTranslationElementProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ELEMENT-REF":
                setattr(obj, "element_ref", ARRef.deserialize(child))
            elif tag == "FILTER":
                setattr(obj, "filter", SerializationHelper.deserialize_by_tag(child, "DataFilter"))
            elif tag == "TRANSMISSION":
                setattr(obj, "transmission", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class SignalServiceTranslationElementPropsBuilder(IdentifiableBuilder):
    """Builder for SignalServiceTranslationElementProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SignalServiceTranslationElementProps = SignalServiceTranslationElementProps()


    def with_element(self, value: Optional[DataPrototype]) -> "SignalServiceTranslationElementPropsBuilder":
        """Set element attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.element = value
        return self

    def with_filter(self, value: Optional[DataFilter]) -> "SignalServiceTranslationElementPropsBuilder":
        """Set filter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.filter = value
        return self

    def with_transmission(self, value: Optional[Boolean]) -> "SignalServiceTranslationElementPropsBuilder":
        """Set transmission attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.transmission = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "element",
        "filter",
        "transmission",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SignalServiceTranslationElementProps:
        """Build and return the SignalServiceTranslationElementProps instance with validation."""
        self._validate_instance()
        return self._obj