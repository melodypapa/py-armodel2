"""MsrQueryP2 AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 456)

JSON Source: docs/json/packages/M2_MSR_Documentation_MsrQuery.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_props import (
    MsrQueryProps,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
        DocumentationBlock,
    )



class MsrQueryP2(ARObject):
    """AUTOSAR MsrQueryP2."""

    def __init__(self) -> None:
        """Initialize MsrQueryP2."""
        super().__init__()
        self.msr_query_props: MsrQueryProps = None
        self.msr_query_result: Optional[DocumentationBlock] = None


class MsrQueryP2Builder:
    """Builder for MsrQueryP2."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MsrQueryP2 = MsrQueryP2()

    def build(self) -> MsrQueryP2:
        """Build and return MsrQueryP2 object.

        Returns:
            MsrQueryP2 instance
        """
        # TODO: Add validation
        return self._obj
