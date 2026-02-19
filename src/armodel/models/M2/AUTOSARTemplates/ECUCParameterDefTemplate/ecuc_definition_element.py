"""EcucDefinitionElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 45)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 440)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import (
    EcucScopeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable import (
    Traceable,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_validation_condition import (
        EcucValidationCondition,
    )

from abc import ABC, abstractmethod


class EcucDefinitionElement(Identifiable, ABC):
    """AUTOSAR EcucDefinitionElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    ecuc_cond: Optional[Any]
    ecuc_validations: list[EcucValidationCondition]
    lower_multiplicity: Optional[PositiveInteger]
    related_trace: Optional[Traceable]
    scope: Optional[EcucScopeEnum]
    upper_multiplicity: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EcucDefinitionElement."""
        super().__init__()
        self.ecuc_cond: Optional[Any] = None
        self.ecuc_validations: list[EcucValidationCondition] = []
        self.lower_multiplicity: Optional[PositiveInteger] = None
        self.related_trace: Optional[Traceable] = None
        self.scope: Optional[EcucScopeEnum] = None
        self.upper_multiplicity: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucDefinitionElement":
        """Deserialize XML element to EcucDefinitionElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucDefinitionElement object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ecuc_cond
        child = ARObject._find_child_element(element, "ECUC-COND")
        if child is not None:
            ecuc_cond_value = child.text
            obj.ecuc_cond = ecuc_cond_value

        # Parse ecuc_validations (list)
        obj.ecuc_validations = []
        for child in ARObject._find_all_child_elements(element, "ECUC-VALIDATIONS"):
            ecuc_validations_value = ARObject._deserialize_by_tag(child, "EcucValidationCondition")
            obj.ecuc_validations.append(ecuc_validations_value)

        # Parse lower_multiplicity
        child = ARObject._find_child_element(element, "LOWER-MULTIPLICITY")
        if child is not None:
            lower_multiplicity_value = child.text
            obj.lower_multiplicity = lower_multiplicity_value

        # Parse related_trace
        child = ARObject._find_child_element(element, "RELATED-TRACE")
        if child is not None:
            related_trace_value = ARObject._deserialize_by_tag(child, "Traceable")
            obj.related_trace = related_trace_value

        # Parse scope
        child = ARObject._find_child_element(element, "SCOPE")
        if child is not None:
            scope_value = child.text
            obj.scope = scope_value

        # Parse upper_multiplicity
        child = ARObject._find_child_element(element, "UPPER-MULTIPLICITY")
        if child is not None:
            upper_multiplicity_value = child.text
            obj.upper_multiplicity = upper_multiplicity_value

        return obj



class EcucDefinitionElementBuilder:
    """Builder for EcucDefinitionElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucDefinitionElement = EcucDefinitionElement()

    def build(self) -> EcucDefinitionElement:
        """Build and return EcucDefinitionElement object.

        Returns:
            EcucDefinitionElement instance
        """
        # TODO: Add validation
        return self._obj
