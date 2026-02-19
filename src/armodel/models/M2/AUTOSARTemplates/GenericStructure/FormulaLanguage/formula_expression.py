"""FormulaExpression AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 223)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 73)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 448)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_FormulaLanguage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from abc import ABC, abstractmethod


class FormulaExpression(ARObject, ABC):
    """AUTOSAR FormulaExpression."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    atp_reference_refs: list[ARRef]
    atp_string_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize FormulaExpression."""
        super().__init__()
        self.atp_reference_refs: list[ARRef] = []
        self.atp_string_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FormulaExpression":
        """Deserialize XML element to FormulaExpression object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FormulaExpression object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse atp_reference_refs (list)
        obj.atp_reference_refs = []
        for child in ARObject._find_all_child_elements(element, "ATP-REFERENCES"):
            atp_reference_refs_value = ARObject._deserialize_by_tag(child, "Referrable")
            obj.atp_reference_refs.append(atp_reference_refs_value)

        # Parse atp_string_refs (list)
        obj.atp_string_refs = []
        for child in ARObject._find_all_child_elements(element, "ATP-STRINGS"):
            atp_string_refs_value = ARObject._deserialize_by_tag(child, "Referrable")
            obj.atp_string_refs.append(atp_string_refs_value)

        return obj



class FormulaExpressionBuilder:
    """Builder for FormulaExpression."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FormulaExpression = FormulaExpression()

    def build(self) -> FormulaExpression:
        """Build and return FormulaExpression object.

        Returns:
            FormulaExpression instance
        """
        # TODO: Add validation
        return self._obj
