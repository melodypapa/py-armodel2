"""NvDataPortAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class NvDataPortAnnotation(GeneralAnnotation):
    """AUTOSAR NvDataPortAnnotation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    variable_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize NvDataPortAnnotation."""
        super().__init__()
        self.variable_ref: Optional[ARRef] = None


class NvDataPortAnnotationBuilder:
    """Builder for NvDataPortAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NvDataPortAnnotation = NvDataPortAnnotation()

    def build(self) -> NvDataPortAnnotation:
        """Build and return NvDataPortAnnotation object.

        Returns:
            NvDataPortAnnotation instance
        """
        # TODO: Add validation
        return self._obj
