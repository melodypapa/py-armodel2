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

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.data_constr_rule import (
    DataConstrRule,
)


class DataConstr(ARElement):
    """AUTOSAR DataConstr."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_constr_rules: list[DataConstrRule]
    def __init__(self) -> None:
        """Initialize DataConstr."""
        super().__init__()
        self.data_constr_rules: list[DataConstrRule] = []

    def serialize(self) -> ET.Element:
        """Serialize DataConstr to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataConstr, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_constr_rules (list to container "DATA-CONSTR-RULES")
        if self.data_constr_rules:
            wrapper = ET.Element("DATA-CONSTR-RULES")
            for item in self.data_constr_rules:
                serialized = ARObject._serialize_item(item, "DataConstrRule")
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

        # Parse data_constr_rules (list from container "DATA-CONSTR-RULES")
        obj.data_constr_rules = []
        container = ARObject._find_child_element(element, "DATA-CONSTR-RULES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_constr_rules.append(child_value)

        return obj



class DataConstrBuilder:
    """Builder for DataConstr."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataConstr = DataConstr()

    def build(self) -> DataConstr:
        """Build and return DataConstr object.

        Returns:
            DataConstr instance
        """
        # TODO: Add validation
        return self._obj
