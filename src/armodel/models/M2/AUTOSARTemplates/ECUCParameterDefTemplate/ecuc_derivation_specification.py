"""EcucDerivationSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 87)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_query import (
    EcucQuery,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Formula.ml_formula import (
    MlFormula,
)


class EcucDerivationSpecification(ARObject):
    """AUTOSAR EcucDerivationSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    calculation: Optional[Any]
    ecuc_queries: list[EcucQuery]
    informal_formula: Optional[MlFormula]
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
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize calculation
        if self.calculation is not None:
            serialized = ARObject._serialize_item(self.calculation, "Any")
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

        # Serialize ecuc_queries (list to container "ECUC-QUERIES")
        if self.ecuc_queries:
            wrapper = ET.Element("ECUC-QUERIES")
            for item in self.ecuc_queries:
                serialized = ARObject._serialize_item(item, "EcucQuery")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize informal_formula
        if self.informal_formula is not None:
            serialized = ARObject._serialize_item(self.informal_formula, "MlFormula")
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse calculation
        child = ARObject._find_child_element(element, "CALCULATION")
        if child is not None:
            calculation_value = child.text
            obj.calculation = calculation_value

        # Parse ecuc_queries (list from container "ECUC-QUERIES")
        obj.ecuc_queries = []
        container = ARObject._find_child_element(element, "ECUC-QUERIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ecuc_queries.append(child_value)

        # Parse informal_formula
        child = ARObject._find_child_element(element, "INFORMAL-FORMULA")
        if child is not None:
            informal_formula_value = ARObject._deserialize_by_tag(child, "MlFormula")
            obj.informal_formula = informal_formula_value

        return obj



class EcucDerivationSpecificationBuilder:
    """Builder for EcucDerivationSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucDerivationSpecification = EcucDerivationSpecification()

    def build(self) -> EcucDerivationSpecification:
        """Build and return EcucDerivationSpecification object.

        Returns:
            EcucDerivationSpecification instance
        """
        # TODO: Add validation
        return self._obj
