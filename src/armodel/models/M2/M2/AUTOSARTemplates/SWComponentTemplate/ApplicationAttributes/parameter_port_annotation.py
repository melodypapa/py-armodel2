"""ParameterPortAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 158)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)


class ParameterPortAnnotation(GeneralAnnotation):
    """AUTOSAR ParameterPortAnnotation."""

    def __init__(self) -> None:
        """Initialize ParameterPortAnnotation."""
        super().__init__()
        self.parameter: Optional[ParameterDataPrototype] = None


class ParameterPortAnnotationBuilder:
    """Builder for ParameterPortAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ParameterPortAnnotation = ParameterPortAnnotation()

    def build(self) -> ParameterPortAnnotation:
        """Build and return ParameterPortAnnotation object.

        Returns:
            ParameterPortAnnotation instance
        """
        # TODO: Add validation
        return self._obj
