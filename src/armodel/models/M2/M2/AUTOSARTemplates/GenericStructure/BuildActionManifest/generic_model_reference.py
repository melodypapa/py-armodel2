"""GenericModelReference AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 449)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_BuildActionManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    Ref,
)


class GenericModelReference(ARObject):
    """AUTOSAR GenericModelReference."""

    def __init__(self) -> None:
        """Initialize GenericModelReference."""
        super().__init__()
        self.base: NameToken = None
        self.dest: NameToken = None
        self.ref: Ref = None


class GenericModelReferenceBuilder:
    """Builder for GenericModelReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GenericModelReference = GenericModelReference()

    def build(self) -> GenericModelReference:
        """Build and return GenericModelReference object.

        Returns:
            GenericModelReference instance
        """
        # TODO: Add validation
        return self._obj
