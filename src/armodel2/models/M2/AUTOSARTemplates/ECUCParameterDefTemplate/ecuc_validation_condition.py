"""EcucValidationCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_condition_formula import (
        EcucConditionFormula,
    )
    from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_query import (
        EcucQuery,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class EcucValidationCondition(Identifiable):
    """AUTOSAR EcucValidationCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECUC-VALIDATION-CONDITION"


    ecuc_queries: list[EcucQuery]
    validation: Optional[EcucConditionFormula]
    _DESERIALIZE_DISPATCH = {
        "ECUC-QUERYS": lambda obj, elem: obj.ecuc_queries.append(SerializationHelper.deserialize_by_tag(elem, "EcucQuery")),
        "VALIDATION": lambda obj, elem: setattr(obj, "validation", SerializationHelper.deserialize_by_tag(elem, "EcucConditionFormula")),
    }


    def __init__(self) -> None:
        """Initialize EcucValidationCondition."""
        super().__init__()
        self.ecuc_queries: list[EcucQuery] = []
        self.validation: Optional[EcucConditionFormula] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucValidationCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucValidationCondition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ecuc_queries (list to container "ECUC-QUERYS")
        if self.ecuc_queries:
            wrapper = ET.Element("ECUC-QUERYS")
            for item in self.ecuc_queries:
                serialized = SerializationHelper.serialize_item(item, "EcucQuery")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize validation
        if self.validation is not None:
            serialized = SerializationHelper.serialize_item(self.validation, "EcucConditionFormula")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALIDATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucValidationCondition":
        """Deserialize XML element to EcucValidationCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucValidationCondition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucValidationCondition, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ECUC-QUERYS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.ecuc_queries.append(SerializationHelper.deserialize_by_tag(item_elem, "EcucQuery"))
            elif tag == "VALIDATION":
                setattr(obj, "validation", SerializationHelper.deserialize_by_tag(child, "EcucConditionFormula"))

        return obj



class EcucValidationConditionBuilder(IdentifiableBuilder):
    """Builder for EcucValidationCondition with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucValidationCondition = EcucValidationCondition()


    def with_ecuc_queries(self, items: list[EcucQuery]) -> "EcucValidationConditionBuilder":
        """Set ecuc_queries list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ecuc_queries = list(items) if items else []
        return self

    def with_validation(self, value: Optional[EcucConditionFormula]) -> "EcucValidationConditionBuilder":
        """Set validation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.validation = value
        return self


    def add_ecuc_query(self, item: EcucQuery) -> "EcucValidationConditionBuilder":
        """Add a single item to ecuc_queries list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ecuc_queries.append(item)
        return self

    def clear_ecuc_queries(self) -> "EcucValidationConditionBuilder":
        """Clear all items from ecuc_queries list.

        Returns:
            self for method chaining
        """
        self._obj.ecuc_queries = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "ecucQuery",
        "validation",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EcucValidationCondition:
        """Build and return the EcucValidationCondition instance with validation."""
        self._validate_instance()
        return self._obj