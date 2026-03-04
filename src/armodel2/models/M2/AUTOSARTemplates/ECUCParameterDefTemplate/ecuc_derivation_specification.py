"""EcucDerivationSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 87)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_query import (
    EcucQuery,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.Formula.ml_formula import (
    MlFormula,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucDerivationSpecification(ARObject):
    """AUTOSAR EcucDerivationSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECUC-DERIVATION-SPECIFICATION"


    calculation: Optional[Any]
    ecuc_queries: list[EcucQuery]
    informal_formula: Optional[MlFormula]
    _DESERIALIZE_DISPATCH = {
        "CALCULATION": lambda obj, elem: setattr(obj, "calculation", SerializationHelper.deserialize_by_tag(elem, "any (EcucParameter)")),
        "ECUC-QUERYS": lambda obj, elem: obj.ecuc_queries.append(SerializationHelper.deserialize_by_tag(elem, "EcucQuery")),
        "INFORMAL-FORMULA": lambda obj, elem: setattr(obj, "informal_formula", SerializationHelper.deserialize_by_tag(elem, "MlFormula")),
    }


    def __init__(self) -> None:
        """Initialize EcucDerivationSpecification."""
        super().__init__()
        self.calculation: Optional[Any] = None
        self.ecuc_queries: list[EcucQuery] = []
        self.informal_formula: Optional[MlFormula] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucDerivationSpecification to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucDerivationSpecification, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize calculation
        if self.calculation is not None:
            serialized = SerializationHelper.serialize_item(self.calculation, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CALCULATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecuc_queries (list to container "ECUC-QUERYS")
        if self.ecuc_queries:
            wrapper = ET.Element("ECUC-QUERYS")
            for item in self.ecuc_queries:
                serialized = SerializationHelper.serialize_item(item, "EcucQuery")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize informal_formula
        if self.informal_formula is not None:
            serialized = SerializationHelper.serialize_item(self.informal_formula, "MlFormula")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INFORMAL-FORMULA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucDerivationSpecification":
        """Deserialize XML element to EcucDerivationSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucDerivationSpecification object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucDerivationSpecification, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CALCULATION":
                setattr(obj, "calculation", SerializationHelper.deserialize_by_tag(child, "any (EcucParameter)"))
            elif tag == "ECUC-QUERYS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.ecuc_queries.append(SerializationHelper.deserialize_by_tag(item_elem, "EcucQuery"))
            elif tag == "INFORMAL-FORMULA":
                setattr(obj, "informal_formula", SerializationHelper.deserialize_by_tag(child, "MlFormula"))

        return obj



class EcucDerivationSpecificationBuilder(BuilderBase):
    """Builder for EcucDerivationSpecification with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucDerivationSpecification = EcucDerivationSpecification()


    def with_calculation(self, value: Optional[any (EcucParameter)]) -> "EcucDerivationSpecificationBuilder":
        """Set calculation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.calculation = value
        return self

    def with_ecuc_queries(self, items: list[EcucQuery]) -> "EcucDerivationSpecificationBuilder":
        """Set ecuc_queries list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ecuc_queries = list(items) if items else []
        return self

    def with_informal_formula(self, value: Optional[MlFormula]) -> "EcucDerivationSpecificationBuilder":
        """Set informal_formula attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.informal_formula = value
        return self


    def add_ecuc_query(self, item: EcucQuery) -> "EcucDerivationSpecificationBuilder":
        """Add a single item to ecuc_queries list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ecuc_queries.append(item)
        return self

    def clear_ecuc_queries(self) -> "EcucDerivationSpecificationBuilder":
        """Clear all items from ecuc_queries list.

        Returns:
            self for method chaining
        """
        self._obj.ecuc_queries = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "calculation",
        "ecucQuery",
        "informalFormula",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EcucDerivationSpecification:
        """Build and return the EcucDerivationSpecification instance with validation."""
        self._validate_instance()
        return self._obj