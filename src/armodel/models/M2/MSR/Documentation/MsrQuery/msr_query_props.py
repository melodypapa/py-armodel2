"""MsrQueryProps AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 344)

JSON Source: docs/json/packages/M2_MSR_Documentation_MsrQuery.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_arg import (
    MsrQueryArg,
)


class MsrQueryProps(ARObject):
    """AUTOSAR MsrQueryProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "comment": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # comment
        "msr_query_args": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=MsrQueryArg,
        ),  # msrQueryArgs
        "msr_query_name": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # msrQueryName
    }

    def __init__(self) -> None:
        """Initialize MsrQueryProps."""
        super().__init__()
        self.comment: Optional[String] = None
        self.msr_query_args: list[MsrQueryArg] = []
        self.msr_query_name: String = None


class MsrQueryPropsBuilder:
    """Builder for MsrQueryProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MsrQueryProps = MsrQueryProps()

    def build(self) -> MsrQueryProps:
        """Build and return MsrQueryProps object.

        Returns:
            MsrQueryProps instance
        """
        # TODO: Add validation
        return self._obj
