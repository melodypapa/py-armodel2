"""UserDefinedTransformationISignalProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 828)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class UserDefinedTransformationISignalProps(ARObject):
    """AUTOSAR UserDefinedTransformationISignalProps."""

    def __init__(self) -> None:
        """Initialize UserDefinedTransformationISignalProps."""
        super().__init__()


class UserDefinedTransformationISignalPropsBuilder:
    """Builder for UserDefinedTransformationISignalProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedTransformationISignalProps = UserDefinedTransformationISignalProps()

    def build(self) -> UserDefinedTransformationISignalProps:
        """Build and return UserDefinedTransformationISignalProps object.

        Returns:
            UserDefinedTransformationISignalProps instance
        """
        # TODO: Add validation
        return self._obj
