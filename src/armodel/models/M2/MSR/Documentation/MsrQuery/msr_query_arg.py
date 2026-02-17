"""MsrQueryArg AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 344)

JSON Source: docs/json/packages/M2_MSR_Documentation_MsrQuery.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)


class MsrQueryArg(ARObject):
    """AUTOSAR MsrQueryArg."""

    arg: String
    si: NameToken
    def __init__(self) -> None:
        """Initialize MsrQueryArg."""
        super().__init__()
        self.arg: String = None
        self.si: NameToken = None


class MsrQueryArgBuilder:
    """Builder for MsrQueryArg."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MsrQueryArg = MsrQueryArg()

    def build(self) -> MsrQueryArg:
        """Build and return MsrQueryArg object.

        Returns:
            MsrQueryArg instance
        """
        # TODO: Add validation
        return self._obj
