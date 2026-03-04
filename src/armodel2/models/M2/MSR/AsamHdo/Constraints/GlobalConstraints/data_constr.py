"""DataConstr AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 310)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 405)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 44)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 179)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Constraints_GlobalConstraints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.data_constr_rule import (
    DataConstrRule,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DataConstr(ARElement):
    """AUTOSAR DataConstr."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DATA-CONSTR"


    data_constr_rules: list[DataConstrRule]
    _DESERIALIZE_DISPATCH = {
        "DATA-CONSTR-RULES": lambda obj, elem: obj.data_constr_rules.append(SerializationHelper.deserialize_by_tag(elem, "DataConstrRule")),
    }


    def __init__(self) -> None:
        """Initialize DataConstr."""
        super().__init__()
        self.data_constr_rules: list[DataConstrRule] = []

    def serialize(self) -> ET.Element:
        """Serialize DataConstr to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataConstr, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_constr_rules (list to container "DATA-CONSTR-RULES")
        if self.data_constr_rules:
            wrapper = ET.Element("DATA-CONSTR-RULES")
            for item in self.data_constr_rules:
                serialized = SerializationHelper.serialize_item(item, "DataConstrRule")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataConstr":
        """Deserialize XML element to DataConstr object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataConstr object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataConstr, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-CONSTR-RULES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.data_constr_rules.append(SerializationHelper.deserialize_by_tag(item_elem, "DataConstrRule"))

        return obj



class DataConstrBuilder(ARElementBuilder):
    """Builder for DataConstr with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DataConstr = DataConstr()


    def with_data_constr_rules(self, items: list[DataConstrRule]) -> "DataConstrBuilder":
        """Set data_constr_rules list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_constr_rules = list(items) if items else []
        return self


    def add_data_constr_rule(self, item: DataConstrRule) -> "DataConstrBuilder":
        """Add a single item to data_constr_rules list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_constr_rules.append(item)
        return self

    def clear_data_constr_rules(self) -> "DataConstrBuilder":
        """Clear all items from data_constr_rules list.

        Returns:
            self for method chaining
        """
        self._obj.data_constr_rules = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataConstrRule",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DataConstr:
        """Build and return the DataConstr instance with validation."""
        self._validate_instance()
        return self._obj