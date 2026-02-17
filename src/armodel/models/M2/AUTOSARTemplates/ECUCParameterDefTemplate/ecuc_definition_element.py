"""EcucDefinitionElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 45)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 440)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_validation_condition import (
    EcucValidationCondition,
)
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable import (
    Traceable,
)


class EcucDefinitionElement(Identifiable):
    """AUTOSAR EcucDefinitionElement."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ecuc_cond": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (EcucCondition),
        ),  # ecucCond
        "ecuc_validations": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=EcucValidationCondition,
        ),  # ecucValidations
        "lower_multiplicity": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # lowerMultiplicity
        "related_trace": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Traceable,
        ),  # relatedTrace
        "scope": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EcucScopeEnum,
        ),  # scope
        "upper_multiplicity": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # upperMultiplicity
    }

    def __init__(self) -> None:
        """Initialize EcucDefinitionElement."""
        super().__init__()
        self.ecuc_cond: Optional[Any] = None
        self.ecuc_validations: list[EcucValidationCondition] = []
        self.lower_multiplicity: Optional[PositiveInteger] = None
        self.related_trace: Optional[Traceable] = None
        self.scope: Optional[EcucScopeEnum] = None
        self.upper_multiplicity: Optional[Boolean] = None


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
