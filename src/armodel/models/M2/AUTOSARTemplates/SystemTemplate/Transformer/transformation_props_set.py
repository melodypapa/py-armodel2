"""TransformationPropsSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 782)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_props import (
    TransformationProps,
)


class TransformationPropsSet(ARElement):
    """AUTOSAR TransformationPropsSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    transformation_props_propses: list[TransformationProps]
    def __init__(self) -> None:
        """Initialize TransformationPropsSet."""
        super().__init__()
        self.transformation_props_propses: list[TransformationProps] = []


class TransformationPropsSetBuilder:
    """Builder for TransformationPropsSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransformationPropsSet = TransformationPropsSet()

    def build(self) -> TransformationPropsSet:
        """Build and return TransformationPropsSet object.

        Returns:
            TransformationPropsSet instance
        """
        # TODO: Add validation
        return self._obj
