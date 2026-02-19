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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    msr_query_props: MsrQueryProps
    msr_query_result: Optional[DocumentationBlock]
    def __init__(self) -> None:
        """Initialize MsrQueryP2."""
        super().__init__()
        self.msr_query_props: MsrQueryProps = None
        self.msr_query_result: Optional[DocumentationBlock] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "MsrQueryP2":
        """Deserialize XML element to MsrQueryP2 object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MsrQueryP2 object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse msr_query_props
        child = ARObject._find_child_element(element, "MSR-QUERY-PROPS")
        if child is not None:
            msr_query_props_value = ARObject._deserialize_by_tag(child, "MsrQueryProps")
            obj.msr_query_props = msr_query_props_value

        # Parse msr_query_result
        child = ARObject._find_child_element(element, "MSR-QUERY-RESULT")
        if child is not None:
            msr_query_result_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.msr_query_result = msr_query_result_value

        return obj



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
