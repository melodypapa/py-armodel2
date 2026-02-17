"""UserDefinedTransformationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 829)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_props import (
    TransformationProps,
)


class UserDefinedTransformationProps(TransformationProps):
    """AUTOSAR UserDefinedTransformationProps."""

    def __init__(self) -> None:
        """Initialize UserDefinedTransformationProps."""
        super().__init__()


class UserDefinedTransformationPropsBuilder:
    """Builder for UserDefinedTransformationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedTransformationProps = UserDefinedTransformationProps()

    def build(self) -> UserDefinedTransformationProps:
        """Build and return UserDefinedTransformationProps object.

        Returns:
            UserDefinedTransformationProps instance
        """
        # TODO: Add validation
        return self._obj
