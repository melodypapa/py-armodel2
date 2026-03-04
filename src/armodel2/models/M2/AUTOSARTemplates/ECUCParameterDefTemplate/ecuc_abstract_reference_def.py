"""EcucAbstractReferenceDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 71)

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
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucAbstractReferenceDef(EcucCommonAttributes, ABC):
    """AUTOSAR EcucAbstractReferenceDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    with_auto: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "WITH-AUTO": lambda obj, elem: setattr(obj, "with_auto", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize EcucAbstractReferenceDef."""
        super().__init__()
        self.with_auto: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucAbstractReferenceDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucAbstractReferenceDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

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
    def deserialize(cls, element: ET.Element) -> "EcucAbstractReferenceDef":
        """Deserialize XML element to EcucAbstractReferenceDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucAbstractReferenceDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucAbstractReferenceDef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "WITH-AUTO":
                setattr(obj, "with_auto", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class EcucAbstractReferenceDefBuilder(EcucCommonAttributesBuilder):
    """Builder for EcucAbstractReferenceDef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucAbstractReferenceDef = EcucAbstractReferenceDef()


    def with_with_auto(self, value: Optional[Boolean]) -> "EcucAbstractReferenceDefBuilder":
        """Set with_auto attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.with_auto = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
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
    def build(self) -> EcucAbstractReferenceDef:
        """Build and return the EcucAbstractReferenceDef instance (abstract)."""
        raise NotImplementedError