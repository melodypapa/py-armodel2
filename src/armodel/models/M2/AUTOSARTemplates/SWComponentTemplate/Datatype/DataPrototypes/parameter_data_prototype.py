"""ParameterDataPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 107)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 310)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2042)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 457)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_DataPrototypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



class ParameterDataPrototype(AutosarDataPrototype):
    """AUTOSAR ParameterDataPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    init_value: Optional[ValueSpecification]
    def __init__(self) -> None:
        """Initialize ParameterDataPrototype."""
        super().__init__()
        self.init_value: Optional[ValueSpecification] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ParameterDataPrototype":
        """Deserialize XML element to ParameterDataPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ParameterDataPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ParameterDataPrototype, cls).deserialize(element)

        # Parse init_value
        child = ARObject._find_child_element(element, "INIT-VALUE")
        if child is not None:
            init_value_value = ARObject._deserialize_by_tag(child, "ValueSpecification")
            obj.init_value = init_value_value

        return obj



class ParameterDataPrototypeBuilder:
    """Builder for ParameterDataPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ParameterDataPrototype = ParameterDataPrototype()

    def build(self) -> ParameterDataPrototype:
        """Build and return ParameterDataPrototype object.

        Returns:
            ParameterDataPrototype instance
        """
        # TODO: Add validation
        return self._obj
