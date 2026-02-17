"""ImplementationElementInParameterInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 184)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)


class ImplementationElementInParameterInstanceRef(ARObject):
    """AUTOSAR ImplementationElementInParameterInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "context": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ParameterDataPrototype,
        ),  # context
        "target": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # target
    }

    def __init__(self) -> None:
        """Initialize ImplementationElementInParameterInstanceRef."""
        super().__init__()
        self.context: Optional[ParameterDataPrototype] = None
        self.target: Optional[Any] = None


class ImplementationElementInParameterInstanceRefBuilder:
    """Builder for ImplementationElementInParameterInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ImplementationElementInParameterInstanceRef = ImplementationElementInParameterInstanceRef()

    def build(self) -> ImplementationElementInParameterInstanceRef:
        """Build and return ImplementationElementInParameterInstanceRef object.

        Returns:
            ImplementationElementInParameterInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
