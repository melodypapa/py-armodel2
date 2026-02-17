"""SwDataDependencyArgs AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 374)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DataDefProperties.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_calprm_ref_proxy import (
    SwCalprmRefProxy,
)
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_variable_ref_proxy import (
    SwVariableRefProxy,
)


class SwDataDependencyArgs(ARObject):
    """AUTOSAR SwDataDependencyArgs."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "sw_calprm_ref_proxy": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwCalprmRefProxy,
        ),  # swCalprmRefProxy
        "sw_variable_ref_proxy": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwVariableRefProxy,
        ),  # swVariableRefProxy
    }

    def __init__(self) -> None:
        """Initialize SwDataDependencyArgs."""
        super().__init__()
        self.sw_calprm_ref_proxy: Optional[SwCalprmRefProxy] = None
        self.sw_variable_ref_proxy: Optional[SwVariableRefProxy] = None


class SwDataDependencyArgsBuilder:
    """Builder for SwDataDependencyArgs."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwDataDependencyArgs = SwDataDependencyArgs()

    def build(self) -> SwDataDependencyArgs:
        """Build and return SwDataDependencyArgs object.

        Returns:
            SwDataDependencyArgs instance
        """
        # TODO: Add validation
        return self._obj
