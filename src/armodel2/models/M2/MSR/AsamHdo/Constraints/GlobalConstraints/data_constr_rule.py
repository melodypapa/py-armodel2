"""DataConstrRule AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 405)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 45)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Constraints_GlobalConstraints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.internal_constrs import (
    InternalConstrs,
)
from armodel2.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.phys_constrs import (
    PhysConstrs,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DataConstrRule(ARObject):
    """AUTOSAR DataConstrRule."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DATA-CONSTR-RULE"


    constr_level: Optional[Integer]
    internal_constrs: Optional[InternalConstrs]
    phys_constrs: Optional[PhysConstrs]
    _DESERIALIZE_DISPATCH = {
        "CONSTR-LEVEL": lambda obj, elem: setattr(obj, "constr_level", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "INTERNAL-CONSTRS": lambda obj, elem: setattr(obj, "internal_constrs", SerializationHelper.deserialize_by_tag(elem, "InternalConstrs")),
        "PHYS-CONSTRS": lambda obj, elem: setattr(obj, "phys_constrs", SerializationHelper.deserialize_by_tag(elem, "PhysConstrs")),
    }


    def __init__(self) -> None:
        """Initialize DataConstrRule."""
        super().__init__()
        self.constr_level: Optional[Integer] = None
        self.internal_constrs: Optional[InternalConstrs] = None
        self.phys_constrs: Optional[PhysConstrs] = None

    def serialize(self) -> ET.Element:
        """Serialize DataConstrRule to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataConstrRule, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize constr_level
        if self.constr_level is not None:
            serialized = SerializationHelper.serialize_item(self.constr_level, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONSTR-LEVEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize internal_constrs
        if self.internal_constrs is not None:
            serialized = SerializationHelper.serialize_item(self.internal_constrs, "InternalConstrs")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTERNAL-CONSTRS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize phys_constrs
        if self.phys_constrs is not None:
            serialized = SerializationHelper.serialize_item(self.phys_constrs, "PhysConstrs")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PHYS-CONSTRS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataConstrRule":
        """Deserialize XML element to DataConstrRule object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataConstrRule object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataConstrRule, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONSTR-LEVEL":
                setattr(obj, "constr_level", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "INTERNAL-CONSTRS":
                setattr(obj, "internal_constrs", SerializationHelper.deserialize_by_tag(child, "InternalConstrs"))
            elif tag == "PHYS-CONSTRS":
                setattr(obj, "phys_constrs", SerializationHelper.deserialize_by_tag(child, "PhysConstrs"))

        return obj



class DataConstrRuleBuilder(BuilderBase):
    """Builder for DataConstrRule with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DataConstrRule = DataConstrRule()


    def with_constr_level(self, value: Optional[Integer]) -> "DataConstrRuleBuilder":
        """Set constr_level attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'constr_level' is required and cannot be None")
        self._obj.constr_level = value
        return self

    def with_internal_constrs(self, value: Optional[InternalConstrs]) -> "DataConstrRuleBuilder":
        """Set internal_constrs attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'internal_constrs' is required and cannot be None")
        self._obj.internal_constrs = value
        return self

    def with_phys_constrs(self, value: Optional[PhysConstrs]) -> "DataConstrRuleBuilder":
        """Set phys_constrs attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'phys_constrs' is required and cannot be None")
        self._obj.phys_constrs = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "constrLevel",
        "internalConstrs",
        "physConstrs",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DataConstrRule:
        """Build and return the DataConstrRule instance with validation."""
        self._validate_instance()
        return self._obj