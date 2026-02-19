"""TransformationISignalProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 772)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    CSTransformerErrorReactionEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from abc import ABC, abstractmethod


class TransformationISignalProps(ARObject, ABC):
    """AUTOSAR TransformationISignalProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    cs_error_reaction: Optional[CSTransformerErrorReactionEnum]
    data_prototype_refs: list[ARRef]
    transformer: Optional[Any]
    def __init__(self) -> None:
        """Initialize TransformationISignalProps."""
        super().__init__()
        self.cs_error_reaction: Optional[CSTransformerErrorReactionEnum] = None
        self.data_prototype_refs: list[ARRef] = []
        self.transformer: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransformationISignalProps":
        """Deserialize XML element to TransformationISignalProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransformationISignalProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse cs_error_reaction
        child = ARObject._find_child_element(element, "CS-ERROR-REACTION")
        if child is not None:
            cs_error_reaction_value = child.text
            obj.cs_error_reaction = cs_error_reaction_value

        # Parse data_prototype_refs (list)
        obj.data_prototype_refs = []
        for child in ARObject._find_all_child_elements(element, "DATA-PROTOTYPES"):
            data_prototype_refs_value = ARObject._deserialize_by_tag(child, "DataPrototype")
            obj.data_prototype_refs.append(data_prototype_refs_value)

        # Parse transformer
        child = ARObject._find_child_element(element, "TRANSFORMER")
        if child is not None:
            transformer_value = child.text
            obj.transformer = transformer_value

        return obj



class TransformationISignalPropsBuilder:
    """Builder for TransformationISignalProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransformationISignalProps = TransformationISignalProps()

    def build(self) -> TransformationISignalProps:
        """Build and return TransformationISignalProps object.

        Returns:
            TransformationISignalProps instance
        """
        # TODO: Add validation
        return self._obj
